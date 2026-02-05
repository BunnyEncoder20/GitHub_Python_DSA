package main

import (
	"fmt"
	"sort"
)

func bruteSortZeroOneTwo(nums []int) []int {
	res := append([]int{}, nums...) // clever way to make a deep copy of copy
	sort.Ints(res)                  // WARN: Foot gun: The func gets a copy of the pointer of the array, hence the original data also gets mutated
	return res
}

func betterSortZeroOneTwo(nums []int) []int {
	// init
	res := make([]int, 0, len(nums))
	count := map[int]int{0: 0, 1: 0, 2: 0}

	// counting the 0,1,2's in the array
	for _, num := range nums {
		count[num]++
	}

	// write the result
	for val := range 3 {
		for range count[val] {
			res = append(res, val)
		}
	}

	return res
}

func optimalSortZeroOneTwo(nums []int) []int {
	// Dutch Flag Algo Summurized
	// 0 region: idx0 to low-1
	// 1 region: low to mid-1
	// unsorted region: mid to high
	// 2 region: high to n-1

	res := append([]int{}, nums...)
	low, mid, high := 0, 0, len(nums)-1

	for mid <= high {
		switch res[mid] {
		case 0:
			res[low], res[mid] = res[mid], res[low]
			low++
			mid++
		case 1:
			mid++
		case 2:
			res[mid], res[high] = res[high], res[mid]
			high--
		}
	}
	return res
}

func main() {
	nums1 := []int{1, 0, 2, 1, 0}
	nums2 := []int{0, 0, 1, 1, 1}

	fmt.Println("Brute Force: Just regular sorting")
	fmt.Println("Nums1", bruteSortZeroOneTwo(nums1))
	fmt.Println("Nums2", bruteSortZeroOneTwo(nums2))

	fmt.Println("Better: Counting:")
	fmt.Println("Nums1:", betterSortZeroOneTwo(nums1))
	fmt.Println("Nums2:", betterSortZeroOneTwo(nums2))

	fmt.Println("Optimal: Dutch Flag Algo:")
	fmt.Println("Nums1:", optimalSortZeroOneTwo(nums1))
	fmt.Println("Nums2:", optimalSortZeroOneTwo(nums2))
}
