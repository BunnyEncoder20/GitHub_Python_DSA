package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"
	"sync"
)

type User struct {
	Name string `json:"name"` // we need this to match the incoming json key to the struct field, otherwise the decoding will fail and we will return a bad request error to the client
}

var userCache = make(map[int]User)

// mutux for thread safety: This one is a read and write lock
// Prevents both reading and writing from happening at the same time.
var cacheMutex sync.RWMutex

func main() {
	// First we need a request multiplexer to route incoming requests to the appropriate handler functions
	// Simply, the handler function redirects the inciming request to the appropriate handler function based on the URL path and HTTP method
	mux := http.NewServeMux()

	// basic template of a handler function
	// First param is the pattern string (http route/endpoint)
	// Second param is the handler for this endpoint, which is a function that takes in an http.ResponseWriter and an http.Request as parameters
	mux.HandleFunc("/", handleRoot)

	// Basic http verb handlers
	mux.HandleFunc("POST /", createUser)
	mux.HandleFunc("GET /user/", getAllUsers)
	mux.HandleFunc("GET /user/{id}", getUser)
	mux.HandleFunc("DELETE /user/{id}", deleteUser)

	// Starting the server on port 8080, and passing in the request multiplexer to handle incoming requests
	log.Println("Server is running on port 8080...")
	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Printf("the server stop bro:\n%s", err.Error())
	}
}

func handleRoot(writer http.ResponseWriter, req *http.Request) {
	// The response write is used to contruct the response to be sent back to the client,
	// and the request is used to read the incoming request from the client like headers, body, etc.
	if _, err := fmt.Fprintf(writer, "Hello World!"); err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		return
	}
}

func createUser(writer http.ResponseWriter, req *http.Request) {
	// We decode the incoming req.body.json so that Go can process the data
	// The body's user structure should match the User struct which we defined above,
	// otherwise the decoding will fail and we will return a bad request error to the client
	var user User
	if err := json.NewDecoder(req.Body).Decode(&user); err != nil {
		http.Error(writer, err.Error(), http.StatusBadRequest)
		return
	}

	if user.Name == "" {
		http.Error(writer, "Name is required", http.StatusBadRequest)
		return
	}

	// writer to the local map db
	cacheMutex.Lock()
	userCache[len(userCache)+1] = user
	log.Printf("User with name:%s created successfully\n", user.Name)
	cacheMutex.Unlock()

	writer.WriteHeader(http.StatusNoContent)
}

func getUser(writer http.ResponseWriter, req *http.Request) {
	// converting the path param from string to int
	idStr := req.PathValue("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(writer, "Invalid user ID", http.StatusBadRequest)
		return
	}

	cacheMutex.RLock() // we are locking the reading part only
	user, ok := userCache[id]
	cacheMutex.RUnlock()
	if !ok {
		http.Error(writer, "User does not exist", http.StatusNotFound)
		return
	}

	// send back the data
	log.Printf("user %s found\n", user.Name)
	userjson, err := json.Marshal(user) // Marshal() created a copy of the user struct as a slice of bytes.
	if err != nil {
		http.Error(writer, err.Error(), http.StatusInternalServerError)
		return
	}
	// NOTE: the more pro way of doing the above is to use json.NewEncoder(writer).Encode(user)
	// which will write the json directly to the response writer, without creating a copy of the user struct as a slice of bytes.
	// This is more efficient and also handles the content type header for us.

	// WARN: Once you call WriteHeader, you cannot change your headers anymore. Go has already sent that part of the packet over the network.
	writer.Header().Set("Content-Type", "application/json")
	writer.WriteHeader(http.StatusOK)
	if _, err := writer.Write(userjson); err != nil {
		// BUG: most likely you cannot do this cause the http.header of ok is already sent
		http.Error(writer, err.Error(), http.StatusInternalServerError)
	}
}

func deleteUser(w http.ResponseWriter, r *http.Request) {
	// getting the id from the path param
	id, err := strconv.Atoi(r.PathValue("id"))
	if err != nil {
		http.Error(w, "Invalid user ID", http.StatusBadRequest)
		return
	}

	// remove the user from the map
	cacheMutex.Lock()
	user, ok := userCache[id]
	if ok {
		delete(userCache, id)
		log.Printf("User with ID:%d | name:%s deleted successfully\n", id, user.Name)
	}
	cacheMutex.Unlock()

	if !ok {
		http.Error(w, "User does not exist", http.StatusNotFound)
		return
	}

	// sending back the deleted user data as a response
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	err = json.NewEncoder(w).Encode(user)
	if err != nil {
		log.Printf("Error encoding user data: %v\n", err)
		return
	}
}

func getAllUsers(w http.ResponseWriter, req *http.Request) {
	// I am making a copy of the map so that it doesn't change while reading it,
	// and can also unlock it as soon as we are done copying it, which allows other operations to happen on the map while we are processing the data.

	cacheMutex.Lock()
	users := make([]User, 0, len(userCache))

	for _, user := range userCache {
		users = append(users, user)
	}
	cacheMutex.Unlock()

	// sending back the data
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	err := json.NewEncoder(w).Encode(users)
	if err != nil {
		log.Printf("Error while encoding users data: %v\n", err)
	}
}
