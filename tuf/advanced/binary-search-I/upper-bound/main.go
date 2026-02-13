package main

import (
	"fmt"
)

func bruteUpperBound(nums []int, x int) int {
	// NOTE: lowerBound is the first element in the sorted array
	// which is greater than or equal to the given x
	for i, num := range nums {
		if num >= x {
			return i
		}
	}

	return len(nums)
}

func optimalUpperBound(nums []int, x int) int {
	// Using simple Binary search
	low, high := 0, len(nums)-1
	ans := len(nums)

	for low <= high {
		mid := (low + high) / 2
		if nums[mid] >= x {
			ans = mid
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return ans
}

func main() {
	x, arr := 2, []int{1, 2, 2, 3}
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, bruteUpperBound(arr, x))   // 1
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, optimalUpperBound(arr, x)) // 1

	x, arr = 9, []int{3, 5, 8, 15, 19}
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, bruteUpperBound(arr, x))   // 3
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, optimalUpperBound(arr, x)) // 1

	x, arr = 3, []int{3, 5, 8, 15, 19}
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, bruteUpperBound(arr, x))   // 0
	fmt.Printf("The upper bound of %d in %v is: %d\n", x, arr, optimalUpperBound(arr, x)) // 1
}
