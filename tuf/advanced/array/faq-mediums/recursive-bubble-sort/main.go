package main

import (
	"fmt"
)

func bubbleSort(nums []int) []int {
	n := len(nums)
	i := n - 1
	bubbleSortHelper(nums, i)
	return nums
}

func bubbleSortHelper(nums []int, i int) {
	if i == 0 {
		// less than equal cause the array might be smaller or equal 1
		return
	}

	swapped := false
	for j := range i {
		if nums[j] > nums[j+1] {
			nums[j], nums[j+1] = nums[j+1], nums[j]
			swapped = true
		}
	}

	// optimization: if not swaps, then the arr is already sorted
	if !swapped {
		return
	}

	bubbleSortHelper(nums, i-1)
}

func main() {
	nums1 := []int{7, 4, 1, 5, 3} // [1, 3, 4, 5, 7]
	nums2 := []int{5, 4, 4, 1, 1} // [1, 1, 4, 4, 5]
	nums3 := []int{3, 2, 3, 4, 5} // [2, 3, 3, 4, 5]

	fmt.Println("Nums1:", bubbleSort(nums1))
	fmt.Println("Nums2:", bubbleSort(nums2))
	fmt.Println("Nums3:", bubbleSort(nums3))
}
