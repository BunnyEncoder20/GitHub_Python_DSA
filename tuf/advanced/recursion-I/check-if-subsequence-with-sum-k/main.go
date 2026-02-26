package main

import "fmt"

func checkSubsequenceSum(nums []int, k int) bool {
	return recursivelyCheckSum(nums, k, 0, []int{})
}

func recursivelyCheckSum(nums []int, target int, i int, subset []int) bool {
	// base case
	if i == len(nums) {
		summ := 0
		for _, num := range subset {
			summ += num
		}

		if summ == target {
			return true
		} else {
			return false
		}
	}

	// take nums[i]
	subset = append(subset, nums[i])
	take := recursivelyCheckSum(nums, target, i+1, subset)
	subset = subset[:len(subset)-1] // removing the last appended element for backtracking

	// not take nums[i]
	nottake := recursivelyCheckSum(nums, target, i+1, subset)

	return take || nottake
}

func optimalCheckSubsequenceSum(nums []int, k int) bool {
	return helperChecker(nums, 0, k)
}

func helperChecker(nums []int, i int, target int) bool {
	// base case: if all the subset is made, check if target was sum was acheieved
	if i == len(nums) {
		return target == 0
	}

	return helperChecker(nums, i+1, target) || helperChecker(nums, i+1, target-nums[i])
}

func main() {
	arr, k := []int{1, 2, 3, 4, 5}, 8
	fmt.Printf("Does one of the subsets of %v sum to %d ? %v\n", arr, k, checkSubsequenceSum(arr, k))
	fmt.Printf("Does one of the subsets of %v sum to %d ? %v\n", arr, k, optimalCheckSubsequenceSum(arr, k))

	arr, k = []int{4, 3, 9, 2}, 10
	fmt.Printf("Does one of the subset of %v sum to %d ? %v\n", arr, k, checkSubsequenceSum(arr, k))
	fmt.Printf("Does one of the subsets of %v sum to %d ? %v\n", arr, k, optimalCheckSubsequenceSum(arr, k))

	arr, k = []int{1, 10, 4, 5}, 16
	fmt.Printf("Does one of the subsets of %v sum to %d ? %v\n", arr, k, checkSubsequenceSum(arr, k))
	fmt.Printf("Does one of the subsets of %v sum to %d ? %v\n", arr, k, optimalCheckSubsequenceSum(arr, k))
}
