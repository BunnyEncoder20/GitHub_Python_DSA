package main

import (
	"fmt"
	"slices"
)

func getTotalTime(bananas []int, rate int) int {
	totalTime := 0
	for _, pile := range bananas {
		totalTime += (pile + rate - 1) / rate // ceil pile/rate without math.Ceil in Go
	}
	return totalTime
}

func bruteMinimumRateToEatBananas(nums []int, timeLimit int) int {
	maxlimit := slices.Max(nums) // get the max element from array

	for i := 1; i <= maxlimit; i++ {
		totalTime := getTotalTime(nums, i)
		// fmt.Printf("For rate of %d, total time take would be %d\n", i, totalTime)
		if totalTime <= timeLimit {
			return i
		}
	}

	return -1 // shouldn't reach here tbh
}

func main() {
	n, nums := 8, []int{7, 15, 6, 3}
	fmt.Printf("Koko can eat all the piles in %d\n", bruteMinimumRateToEatBananas(nums, n))

	n, nums = 5, []int{25, 12, 8, 14, 19}
	fmt.Printf("Koko can eat all the piles in %d\n", bruteMinimumRateToEatBananas(nums, n))

	n, nums = 8, []int{3, 7, 6, 11}
	fmt.Printf("Koko can eat all the piles in %d\n", bruteMinimumRateToEatBananas(nums, n))
}
