package main

import (
	"fmt"
)

func bruteFindMin(nums []int) int {
	ans := 1<<63 - 1 // math.MaxInt
	for _, num := range nums {
		ans = min(num, ans)
	}
	return ans
}

func optimalFindMin(nums []int) int {
	ans := 1<<63 - 1 // math.MaxInt
	low, high := 0, len(nums)-1

	for low <= high {
		mid := (low + high) / 2

		// potential lowest element would be min of sorted half (unsorted)
		// take it and eliminate that half
		if nums[low] <= nums[mid] {
			ans = min(ans, nums[low])
			low = mid + 1
		} else {
			ans = min(ans, nums[mid])
			high = mid - 1
		}
	}

	return ans
}

func main() {
	arr := []int{4, 5, 6, 7, 0, 1, 2, 3}

	fmt.Printf("Then minimum element in %v is %d\n", arr, bruteFindMin(arr))
	fmt.Printf("Then minimum element in %v is %d\n", arr, optimalFindMin(arr))

	arr = []int{3, 4, 5, 1, 2}
	fmt.Printf("Then minimum element in %v is %d\n", arr, bruteFindMin(arr))
	fmt.Printf("Then minimum element in %v is %d\n", arr, optimalFindMin(arr))

	arr = []int{4, 5, 6, 7, -7, 1, 2, 3}
	fmt.Printf("Then minimum element in %v is %d\n", arr, bruteFindMin(arr))
	fmt.Printf("Then minimum element in %v is %d\n", arr, optimalFindMin(arr))
}
