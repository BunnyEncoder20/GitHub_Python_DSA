package main

import (
	"fmt"
	"slices"
)

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
	mpp := make(map[int]int)

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

// Only better if the nums arr is already sorted
func optimalTwoSum(nums []int, target int) [2]int {
	// init
	n := len(nums)
	elementIndexMap := make(map[int]int, n)
	for i, num := range nums {
		elementIndexMap[num] = i
	}
	res := [2]int{}
	left, right := 0, n-1

	// sort the nums array
	slices.Sort(nums)

	// traverse the array to find twoSum
	for left < right {
		// dups are not allowed
		if nums[left] == nums[right] {
			left++
			right--
			continue
		}
		summ := nums[left] + nums[right]
		if summ == target {
			res[0], res[1] = elementIndexMap[nums[left]], elementIndexMap[nums[right]]
			break
		} else if summ < target {
			left++
		} else {
			right--
		}
	}

	return res
}

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
