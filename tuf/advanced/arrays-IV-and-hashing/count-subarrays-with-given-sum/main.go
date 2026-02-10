package main

import (
	"fmt"
)

func bruteCountSubarrayWithSumK(k int, nums []int) int {
	n, count := len(nums), 0

	for i := 0; i < n; i++ {
		sum := 0
		for j := i; j < n; j++ {
			sum += nums[j]
			if sum == k {
				count++
			}
		}
	}

	return count
}

func optimalCountSubarrayWithSumK(k int, nums []int) int {
	preSumMap := make(map[int]int) // stores map[sum]count
	preSumMap[0] = 1               // initially when we do not pick anyone, we have a sum of 0
	prefixSum, totalCount := 0, 0

	for _, num := range nums {
		prefixSum += num
		if count, ok := preSumMap[prefixSum-k]; ok {
			totalCount += count // add all the times that subarray sum has occured
		}
		preSumMap[prefixSum]++ // update the count of the sum
	}

	return totalCount
}

func main() {
	k, nums := 2, []int{1, 1, 1} // 2
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, bruteCountSubarrayWithSumK(k, nums))
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, optimalCountSubarrayWithSumK(k, nums))
	k, nums = 3, []int{1, 2, 3} // 2
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, bruteCountSubarrayWithSumK(k, nums))
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, optimalCountSubarrayWithSumK(k, nums))
	k, nums = 6, []int{3, 1, 2, 4} // 2
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, bruteCountSubarrayWithSumK(k, nums))
	fmt.Printf("Count of Subarray with sum %d in %v is: %d\n", k, nums, optimalCountSubarrayWithSumK(k, nums))
}
