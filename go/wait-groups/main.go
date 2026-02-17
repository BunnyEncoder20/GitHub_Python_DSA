package main

import (
	"fmt"
	"log"
	"math/rand/v2"
	"sync"
	"time"
)

var statusCode = [10]int{200, 202, 203, 400, 403, 404, 409, 500, 501, 502}

func simNetworkCall() (int, string) {
	// sleep for random time between range [0, 30)
	time.Sleep(time.Second * time.Duration(rand.IntN(3)))
	randIdx := rand.IntN(len(statusCode))
	code := statusCode[randIdx]
	err := ""
	if code > 500 {
		err = "There was a internal server"
	}
	return code, err
}

func getStatusCodeNormal(link string) {
	log.Printf("requesting %s ...\n", link)
	code, error := simNetworkCall()
	if error != "" {
		log.Println(error)
	}
	log.Printf("Status code: %d returned from %s\n", code, link)
}

func getStatusCode(link string, wg *sync.WaitGroup) {
	log.Printf("requesting %s ...\n", link)
	code, error := simNetworkCall()
	if error != "" {
		log.Println("There was a error while making the request to ", link)
	}

	log.Printf("Status code: %d returned from %s\n", code, link)
	wg.Done()
}

func main() {
	callLinksSequentially()
	callLinksViaGoroutines()
}

func callLinksSequentially() {
	start := time.Now()
	for _, link := range Links {
		getStatusCodeNormal(link)
	}
	fmt.Printf("Time taken by sequentially to get status code for all links: %s s\n", time.Since(start))
	fmt.Println("-----------------------------------------------------------")
	fmt.Println("-----------------------------------------------------------")
	fmt.Println("-----------------------------------------------------------")
}

func callLinksViaGoroutines() {
	// wait group init
	var wg sync.WaitGroup
	wg.Add(len(Links)) // number of threads we want to wait for

	start := time.Now()
	for _, link := range Links {
		go getStatusCode(link, &wg) // go func makes a GoRoutine, which will execute that function in a separate thread
	}

	// wait group should wait for all threads before exiting the main thread
	wg.Wait()
	fmt.Printf("Time taken by GoRoutine to get status code for all links: %s s\n", time.Since(start))
}

func optimalCallLinksViaGoroutines() {
	var wg sync.WaitGroup

	for _, link := range Links {
		wg.Add(1) // add one thread to wait group for each link

		go func(link string) {
			defer wg.Done()           // mark the thread as done when the function returns
			getStatusCodeNormal(link) // with this way of architecture, we don't need to change the business logic of getStatusCodeNormal, we can reuse it as it is, and we don't need to pass the wait group to it, which is a better design
		}(link) // IIFE: immediately invoked function expression, we need to pass the link as an argument to avoid closure issue
	}
}
