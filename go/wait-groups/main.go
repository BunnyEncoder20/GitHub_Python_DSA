package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

func getStatusCode(link string) {
	res, error := http.Get(link)
	if error != nil {
		fmt.Println("There was a error while making the request to ", link)
		panic(error)
	}

	fmt.Printf("Status code: %d returned from %s\n", res.StatusCode, link)
}

var wg sync.WaitGroup

func main() {
	links := []string{
		"https://youtube.com",
		"https://google.com",
		"https://facebook.com",
		"https://twitter.com",
		"https://linkedin.com",
		"https://github.com",
	}

	start := time.Now()
	for _, link := range links {
		getStatusCode(link)
	}
	fmt.Printf("Time taken by sequentially to get status code for all links: %s s\n", time.Since(start))
}
