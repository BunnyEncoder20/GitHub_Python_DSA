package main

import "fmt"

func powerSet(arr []int) [][]int {
	n := len(arr)
	ans := make([][]int, 0, 1<<n)
	recursiveSubsets(arr, 0, []int{}, &ans)
	return ans
}

func recursiveSubsets(arr []int, i int, subset []int, ans *[][]int) {
	// base case
	if i == len(arr) {
		temp := append([]int{}, subset...)
		*ans = append(*ans, temp)
		return
	}

	// take arr[i]
	subset = append(subset, arr[i])
	recursiveSubsets(arr, i+1, subset, ans)
	subset = subset[:len(subset)-1] // removing the last appended element

	// not take arr[i]
	recursiveSubsets(arr, i+1, subset, ans)
}

func main() {
	arr := []int{1, 2, 3}
	fmt.Printf("The powerSet of %v are: %v\n", arr, powerSet(arr))

	arr = []int{1, 2}
	fmt.Printf("The powerSet of %v are: %v\n", arr, powerSet(arr))

	arr = []int{0}
	fmt.Printf("The powerSet of %v are: %v\n", arr, powerSet(arr))

	arr = []int{-6, -3, -4, 3, -8, 10, -10, -9, -1, 1}
	fmt.Printf("The powerSet of %v are: %v\n", arr, powerSet(arr))
}
