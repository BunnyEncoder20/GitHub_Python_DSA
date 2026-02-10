package main

import (
	"fmt"
)

func bruteLongestSubarrayWithSumK(k int, nums []int) int {
	n, maxLength := len(nums), 0

	for i := 0; i < n; i++ {
		summ := 0
		for j := i; j < n; j++ {
			summ += nums[j]
			if summ == k && (j-i+1) > maxLength {
				maxLength = j - i + 1
			}
		}
	}
	return maxLength
}

func optimalLongestSubarrayWithSumK(k int, nums []int) int {
	preSumMap := make(map[int]int) // stores [sum]idx
	preSum, maxLength := 0, 0

	for i := range nums {
		preSum += nums[i]

		// summ directly equals k
		if preSum == k {
			maxLength = max(maxLength, i+1)
		}

		// check if summ-k is present in the map.
		// if it does, then from that idx to here is a subarray with sum = k
		if idx, ok := preSumMap[preSum-k]; ok {
			lenSubarray := i - idx
			maxLength = max(maxLength, lenSubarray)
		}

		// cause we want longest legnth,
		// we should not overwrite keys to later index
		// hence only adding keys, if they don't exist
		if _, exists := preSumMap[preSum]; !exists {
			preSumMap[preSum] = i
		}
	}
	return maxLength
}

func main() {
	k, nums := 15, []int{10, 5, 2, 7, 1, 9}
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, bruteLongestSubarrayWithSumK(k, nums))
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, optimalLongestSubarrayWithSumK(k, nums))
	k, nums = 6, []int{-3, 2, 1}
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, bruteLongestSubarrayWithSumK(k, nums))
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, optimalLongestSubarrayWithSumK(k, nums))
	k, nums = 1, []int{-1, 1, 1}
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, bruteLongestSubarrayWithSumK(k, nums))
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, optimalLongestSubarrayWithSumK(k, nums))
	k, nums = 5, []int{1, 2, 3, -2, 2, 4, -1, 1, 2, -1}
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, bruteLongestSubarrayWithSumK(k, nums))
	fmt.Printf("Longest Subarray length with sum %d in %v is: %d\n", k, nums, optimalLongestSubarrayWithSumK(k, nums))
}
