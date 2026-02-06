package main

import (
	"fmt"
	"sort"
)

func backtracking(nums []int, start int, res *[][]int) {
	// base case
	if start == len(nums) {
		// NOTE: we could do this>> temp := append([]int{}, nums...) but this one is more readable and understandable
		temp := make([]int, len(nums))
		copy(temp, nums)
		*res = append(*res, temp)
	}

	// swap the start with all the numbers to generate all possibilities
	for i := start; i < len(nums); i++ {
		// swapping the start and ith num
		nums[start], nums[i] = nums[i], nums[start]

		// recursive call for next permutations
		backtracking(nums, start+1, res)

		// putting the nums back to the original place
		nums[start], nums[i] = nums[i], nums[start]
	}
}

func allPermutations(nums []int) [][]int {
	res := [][]int{}
	backtracking(nums, 0, &res)
	return res
}

func comparePermutation(s1, s2 []int) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i := range s1 {
		if s1[i] != s2[i] {
			return false
		}
	}
	return true
}

func bruteNextPermutation(nums []int) []int {
	res := make([]int, 0, len(nums))
	everyPermutation := allPermutations(nums)

	// Sorting all the permutation lexograhically
	sort.Slice(everyPermutation, func(i, j int) bool {
		for k := 0; k < len(everyPermutation[i]); k++ {
			if everyPermutation[i][k] < everyPermutation[j][k] {
				return true
			}
			if everyPermutation[i][k] > everyPermutation[j][k] {
				return false
			}
		}
		return false // fallback, they are the same array
	})

	// Determine the nest Permutation via linear search
	for i := range everyPermutation {
		if comparePermutation(everyPermutation[i], nums) {
			res = append(res, everyPermutation[(i+1)%len(nums)]...)
		}
	}

	return res
}

func reversed(s []int) []int {
	n := len(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func optimalNextPermutation(nums []int) {
	// Longer prefix match, means theh words (or slices in this case) are closer.
	// 1. find the breaking point (where the values start to dip down)
	// 2. find amoung the values which we can change the number which is JUST greater than breaking point number (so that we get the very next Permutation)
	// 3. Trying to place the values is sorted order to get the very next possible permutation
	n := len(nums)

	// finding the dip point
	dipIdx := -1
	for i := n - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			dipIdx = i
			break
		}
	}

	// edge case (there was no dip, sorted in decreasing order)
	if dipIdx == -1 {
		reversed(nums)
		return
	}

	// finding the element just greater than the dip element
	for i := n - 1; i > dipIdx; i-- {
		if nums[i] > nums[dipIdx] {
			// swap these two places
			nums[i], nums[dipIdx] = nums[dipIdx], nums[i]
			break
		}
	}

	// reverse the elements before the dipIdx to get the immedeate next permutation
	reversed(nums[dipIdx+1:])
}

func main() {
	nums1 := []int{1, 2, 3}
	fmt.Println("Brute Force:")
	fmt.Print("Given array: ", nums1)
	fmt.Println(" | Next Permutations: ", bruteNextPermutation(nums1))
	nums2 := []int{3, 2, 1}
	fmt.Print("Given array: ", nums2)
	fmt.Println(" | Next Permutations: ", bruteNextPermutation(nums2))

	fmt.Println("Optimal Approch:")
	fmt.Print("Given array: ", nums1)
	optimalNextPermutation(nums1)
	fmt.Println(" | Next Permutations: ", nums1)
	fmt.Print("Given array: ", nums2)
	optimalNextPermutation(nums2)
	fmt.Println(" | Next Permutations: ", nums2)
}
