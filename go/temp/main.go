package main

import (
	"fmt"
)

func main() {
	var i interface{} = "hello"

	s, ok := i.(string)
	if ok {
		fmt.Println(s, ok) // Output: hello true
	}

	f, ok := i.(float64)
	fmt.Println(f, ok) // Output: 0 false (f is the zero value of float64, no panic)
}
