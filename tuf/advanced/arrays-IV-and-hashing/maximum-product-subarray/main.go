package main

import (
	"fmt"
)

func bruteMaxProduct(nums []int) int {
	maxProduct := -1 << 63
	n := len(nums)

	for i := 0; i < n; i++ {
		prod := 1
		for j := i; j < n; j++ {
			prod *= nums[j]
			if maxProduct < prod {
				maxProduct = prod
			}
		}
	}

	return maxProduct
}

func optimalMaxProduct(nums []int) int {
	// we need to compute the product from the start and from the back
	// if we encounter a zero, we reset the product to 1 and restart (like a new subarray)

	// init
	n := len(nums)
	maxProduct, prefix, suffix := -1<<63, 1, 1

	// iterate over array and compute both pre and suffix
	for i := 0; i < n; i++ {
		if prefix == 0 {
			prefix = 1
		}
		if suffix == 0 {
			suffix = 1
		}

		prefix *= nums[i]
		suffix *= nums[n-1-i]
		if prefix > maxProduct {
			maxProduct = prefix
		}
		if suffix > maxProduct {
			maxProduct = suffix
		}
	}

	return maxProduct
}

func main() {
	nums1 := []int{4, 5, 3, 7, 1, 2}
	nums2 := []int{-5, 0, -2}
	nums3 := []int{4, 0, 2, 3, 0}
	fmt.Println("Brute Force:")
	fmt.Printf("%v | maxProduct = %d\n", nums1, bruteMaxProduct(nums1))
	fmt.Printf("%v | maxProduct = %d\n", nums2, bruteMaxProduct(nums2))
	fmt.Printf("%v | maxProduct = %d\n", nums3, bruteMaxProduct(nums3))

	fmt.Println("Optimal Approach:")
	fmt.Printf("%v | maxProduct = %d\n", nums1, optimalMaxProduct(nums1))
	fmt.Printf("%v | maxProduct = %d\n", nums2, optimalMaxProduct(nums2))
	fmt.Printf("%v | maxProduct = %d\n", nums3, optimalMaxProduct(nums3))
}
