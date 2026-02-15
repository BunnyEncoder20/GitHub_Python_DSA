package main

import (
	"fmt"
	"math"
)

func getMaxNum(nums []int) int {
	maxnum := -1 << 63 // math.MinInt
	for _, num := range nums {
		maxnum = max(maxnum, num)
	}
	return maxnum
}

func getTotal(divisor int, nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += int(math.Ceil(float64(num) / float64(divisor)))
	}
	return sum
}

func bruteSmallestDivisor(nums []int, limit int) int {
	maxNum := getMaxNum(nums)
	for divisor := 1; divisor <= maxNum; divisor++ {
		totalSummation := getTotal(divisor, nums)
		fmt.Printf("If we divide by %d the total summation is: %d\n", divisor, totalSummation)
		if totalSummation <= limit {
			return divisor
		}
	}
	return -1 // should never reach here
}

func optimalSammlestDivisor(nums []int, limit int) int {
	// cause we need to go through sorted nums 1...max(nums)
	// We can implement binary search
	low, high := 1, getMaxNum(nums)
	ans := getMaxNum(nums)

	for low <= high {
		mid := (low + high) / 2

		totalSummation := getTotal(mid, nums)
		if totalSummation <= limit {
			ans = mid
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return ans
}

func main() {
	nums, limit := []int{1, 2, 3, 4, 5}, 8
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, bruteSmallestDivisor(nums, limit))
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, optimalSammlestDivisor(nums, limit))

	nums, limit = []int{8, 4, 2, 3}, 10
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, bruteSmallestDivisor(nums, limit))
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, optimalSammlestDivisor(nums, limit))

	nums, limit = []int{8, 4, 2, 3}, 4
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, bruteSmallestDivisor(nums, limit))
	fmt.Printf("Smallest divisor for making %v sum under %d is: %d\n", nums, limit, optimalSammlestDivisor(nums, limit))
}
