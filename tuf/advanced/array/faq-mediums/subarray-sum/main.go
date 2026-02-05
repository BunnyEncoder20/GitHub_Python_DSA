package main

import (
	"fmt"
	"math"
)

func bruteSubArraySum(nums []int) int {
	// Generating all sub arrays and recording the highest sum
	n := len(nums)
	maxSum := math.MinInt

	for i := 0; i < n; i++ {
		sum := 0
		for j := i; j < n; j++ {
			sum += nums[j]
			if sum > maxSum {
				maxSum = sum
			}
		}
	}

	return maxSum
}

func optimalSubArraySum(nums []int) int {
	// Kadane's algorithm
	sum, maxSum := 0, math.MinInt

	for i := range nums {
		sum += nums[i]
		if sum > maxSum {
			maxSum = sum
		}
		if sum < 0 {
			sum = 0
		}
	}

	return maxSum
}

func main() {
	nums1 := []int{2, 3, 5, -2, 7, -4}      // 15
	nums2 := []int{-2, -3, -7, -2, -10, -4} // -2
	nums3 := []int{-1, 2, 3, -1, 2, -6, 5}  // 6

	fmt.Println("Brute force:")
	fmt.Println("nums1", bruteSubArraySum(nums1))
	fmt.Println("nums2", bruteSubArraySum(nums2))
	fmt.Println("nums3", bruteSubArraySum(nums3))

	fmt.Println("Optimal:")
	fmt.Println("nums1", optimalSubArraySum(nums1))
	fmt.Println("nums2", optimalSubArraySum(nums2))
	fmt.Println("nums3", optimalSubArraySum(nums3))
}
