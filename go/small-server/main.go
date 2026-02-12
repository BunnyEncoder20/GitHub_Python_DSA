package main

import (
	"fmt"
	"net/http"
)

func main() {
	// First we need a request multiplexer to route incoming requests to the appropriate handler functions
	// Simply, the handler function redirects the inciming request to the appropriate handler function based on the URL path and HTTP method
	mux := http.NewServeMux()

	// basic template of a handler function
	// First param is the pattern string (http route/endpoint)
	// Second param is the handler for this endpoint, which is a function that takes in an http.ResponseWriter and an http.Request as parameters
	mux.HandleFunc("/", handleRoot)

	// Starting the server on port 8080, and passing in the request multiplexer to handle incoming requests
	fmt.Println("Server is running on port 8080...")
	http.ListenAndServe(":8080", mux)
}

func handleRoot(writer http.ResponseWriter, req *http.Request) {
	// The response write is used to contruct the response to be sent back to the client,
	// and the request is used to read the incoming request from the client like headers, body, etc.
	fmt.Fprintf(writer, "Hello World!")
}
