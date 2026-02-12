package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type User struct {
	Name string `json:"name"` // we need this to match the incoming json key to the struct field, otherwise the decoding will fail and we will return a bad request error to the client
}

var userCache = make(map[int]User)

func main() {
	// First we need a request multiplexer to route incoming requests to the appropriate handler functions
	// Simply, the handler function redirects the inciming request to the appropriate handler function based on the URL path and HTTP method
	mux := http.NewServeMux()

	// basic template of a handler function
	// First param is the pattern string (http route/endpoint)
	// Second param is the handler for this endpoint, which is a function that takes in an http.ResponseWriter and an http.Request as parameters
	mux.HandleFunc("/", handleRoot)

	// Basic post handler
	mux.HandleFunc("POST /", createUser)

	// Starting the server on port 8080, and passing in the request multiplexer to handle incoming requests
	fmt.Println("Server is running on port 8080...")
	http.ListenAndServe(":8080", mux)
}

func handleRoot(writer http.ResponseWriter, req *http.Request) {
	// The response write is used to contruct the response to be sent back to the client,
	// and the request is used to read the incoming request from the client like headers, body, etc.
	fmt.Fprintf(writer, "Hello World!")
}

func createUser(writer http.ResponseWriter, req *http.Request) {
	// We decode the incoming req.body.json so that Go can process the data
	var user User
	err := json.NewDecoder(req.Body).Decode(&user)
	// The body's user structure should match the User struct which we defined above,
	// otherwise the decoding will fail and we will return a bad request error to the client
	if err != nil {
		http.Error(writer, err.Error(), http.StatusBadRequest)
	}

	if user.Name == "" {
		http.Error(writer, "Name is required", http.StatusBadRequest)
		return
	}

	// writer to the local map db
	userCache[len(userCache)+1] = user
	fmt.Println("Users:\n", userCache)

	writer.WriteHeader(http.StatusNoContent)
}
