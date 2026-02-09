package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i, j := m-1, n-1
	k := len(nums1) - 1

	for i >= 0 && j >= 0 {
		if nums1[i] >= nums2[j] {
			nums1[k] = nums1[i]
			i--
		} else if nums1[i] < nums2[j] {
			nums1[k] = nums2[j]
			j--
		}
		k--
	}

	// if any of the elements are still left in nums2, copy them over
	for j >= 0 {
		nums1[k] = nums2[j]
		k--
		j--
	}
}

func main() {
	nums1, nums2 := []int{-5, -2, 4, 5, 0, 0, 0}, []int{-3, 1, 8}
	merge(nums1, 4, nums2, 3)
	fmt.Println(nums1)

	nums1, nums2 = []int{0, 2, 7, 8, 0, 0, 0}, []int{-7, -3, -1}
	merge(nums1, 4, nums2, 3)
	fmt.Println(nums1)

	nums1, nums2 = []int{1, 3, 5, 0, 0, 0, 0}, []int{2, 4, 6, 7}
	merge(nums1, 3, nums2, 4)
	fmt.Println(nums1)
}
