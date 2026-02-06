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

func optimalNextPermutation(nums []int) []int {
	res := make([]int, 0, len(nums))

	return res
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
	fmt.Println(" | Next Permutations: ", optimalNextPermutation(nums1))
	fmt.Print("Given array: ", nums2)
	fmt.Println(" | Next Permutations: ", bruteNextPermutation(nums2))
}
