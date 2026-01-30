package main

import "fmt"

func bruteTwoSum(nums []int, target int) []int {
	n := len(nums)

	for i := range n {
		for j := i + 1; j < n; j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func betterTwoSum(nums []int, target int) []int {
	mpp := make(map[int]int) // using struct cause they have 0 size in memory

	for i, num := range nums {
		moreNeeded := target - num

		if j, exists := mpp[moreNeeded]; exists {
			return []int{j, i} // if the value us there return it's index
		} else {
			mpp[num] = i
		}
	}

	return nil
}

func optimalTwoSum(nums []int, target int) int { return 0 }

func main() {
	nums := []int{1, 6, 2, 10, 3}
	fmt.Println("Nums1:")
	fmt.Println("Brute:", bruteTwoSum(nums, 7))
	fmt.Println("Better:", betterTwoSum(nums, 7))
	fmt.Println("Optimal:", optimalTwoSum(nums, 7))

	nums = []int{1, 3, 5, -7, 6, -3}
	fmt.Println("Nums2")
	fmt.Println("Brute:", bruteTwoSum(nums, 0))
	fmt.Println("Better:", betterTwoSum(nums, 0))
	fmt.Println("Optimal:", optimalTwoSum(nums, 0))

	nums = []int{-6, 7, 1, -7, 6, 2}
	fmt.Println("Brute:", bruteTwoSum(nums, 3))
	fmt.Println("Better:", betterTwoSum(nums, 3))
	fmt.Println("Optimal:", optimalTwoSum(nums, 3))
}
