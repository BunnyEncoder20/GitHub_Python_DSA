package main

import (
	"fmt"
)

func bruteSubarrayWithXorK(nums []int, k int) int {
	n, totalCount := len(nums), 0

	for i := 0; i < n; i++ {
		xor := 0
		for j := i; j < n; j++ {
			xor = xor ^ nums[j]
			if xor == k {
				totalCount++
			}
		}
	}

	return totalCount
}

func optimalSubarrayWithXorK(nums []int, k int) int {
	preXor, preXorMap := 0, make(map[int]int) // stores map[preXor]count
	preXorMap[0] = 1                          // we add xor of 0 at least once, cause we might get preXor directly = k
	totalCount := 0

	for _, num := range nums {
		preXor ^= num

		// x ^ k = preXor
		// x ^ k ^ k = preXor ^ k
		// x = preXor ^ k
		if count, ok := preXorMap[preXor^k]; ok {
			totalCount += count
		}

		// update the map
		preXorMap[preXor]++
	}

	return totalCount
}

func main() {
	a, k := []int{4, 2, 2, 6, 4}, 6
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, bruteSubarrayWithXorK(a, k))   // 4
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, optimalSubarrayWithXorK(a, k)) // 4
	a, k = []int{5, 6, 7, 8, 9}, 5
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, bruteSubarrayWithXorK(a, k))   // 2
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, optimalSubarrayWithXorK(a, k)) // 2
	a, k = []int{5, 2, 9}, 7
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, bruteSubarrayWithXorK(a, k))   // 1
	fmt.Printf("The number of subarrays of %v with XOR equal to %d are: %d\n", a, k, optimalSubarrayWithXorK(a, k)) // 1
}
