package main

import (
	"fmt"
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
	fmt.Println(res)
	return res
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Print("Results:\n", allPermutations(nums))
}
