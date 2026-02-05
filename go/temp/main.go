package main

import (
	"fmt"
	"slices"
)

func main() {
	nums := []int{1, 12, 3}
	copynums := append([]int{}, nums...)
	fmt.Println(nums)
	slices.Sort(copynums)
	fmt.Println("copynums:", copynums)
	fmt.Println("nums:", nums) // footgun
}
