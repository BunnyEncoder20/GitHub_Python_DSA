package main

import (
	"fmt"
)

func bruteSearchInARotatedSortedArray(nums []int, target int) bool {
	for _, num := range nums {
		if num == target {
			return true
		}
	}
	return false
}

func optimalSearchInARotatedSortedArray(nums []int, target int) bool {
	// using bsearch cause the array is already sorted
	low, high := 0, len(nums)-1

	for low <= high {
		mid := (low + high) / 2

		if nums[mid] == target {
			return true
		} else if nums[low] == nums[mid] && nums[mid] == nums[high] {
			// edge case: skipping the duplicates
			low++
			high--
		} else if nums[low] <= nums[mid] {
			// left half is unrotated/sorted

			if nums[low] <= target && target <= nums[mid] {
				// target lies within this range
				high = mid - 1
			} else {
				// target not with this range
				low = mid + 1
			}
		} else {
			// right half is unrotated/sorted

			if nums[mid] <= target && target <= nums[high] {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
	}
	return false
}

func main() {
	arr, target := []int{7, 8, 1, 2, 3, 3, 3, 4, 5, 6}, 3
	if result := bruteSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}
	if result := optimalSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}

	arr, target = []int{7, 8, 1, 2, 3, 3, 3, 4, 5, 6}, 10
	if result := bruteSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}
	if result := optimalSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}

	arr, target = []int{7, 8, 1, 2, 3, 3, 3, 4, 5, 6}, 7
	if result := bruteSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}
	if result := optimalSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}

	arr, target = []int{-62, -62, -59, -59, -59, -41, -41, -39, -39, -38, -38, -28, -28, -27, -27, 11, 20, 20, 20, 35, 54, 54, 69, 69, 74, 74, 74, 77, 84, 84, 93, 93, -96, -96, -94, -94, -94, -66, -65}, -96
	if result := bruteSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}
	if result := optimalSearchInARotatedSortedArray(arr, target); result {
		fmt.Printf("Target found.\n")
	} else {
		fmt.Printf("Target was NOT found.\n")
	}
}
