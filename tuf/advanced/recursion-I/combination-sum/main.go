package main

import (
	"fmt"
)

func combinationSum(candidates []int, target int) [][]int {
	ans := [][]int{}
	recursivelyCheckSum(0, []int{}, target, candidates, &ans)
	return ans
}

func recursivelyCheckSum(i int, currCombo []int, target int, candidates []int, ans *[][]int) {
	// base case
	if target == 0 {
		tmp := append([]int{}, currCombo...)
		*ans = append(*ans, tmp)
		return
	}

	// sum became too large
	if target < 0 {
		return
	}

	// no elements left
	if i == len(candidates) {
		return
	}

	// take or not to take
	recursivelyCheckSum(i+1, currCombo, target, candidates, ans)

	currCombo = append(currCombo, candidates[i])
	target -= candidates[i]
	recursivelyCheckSum(i, currCombo, target, candidates, ans)
}

func main() {
	arr, target := []int{2, 3, 5, 4}, 7
	fmt.Printf("The combinations of %v which sum up to %v are %v\n", arr, target, combinationSum(arr, target))

	arr, target = []int{2}, 1
	fmt.Printf("The combinations of %v which sum up to %v are %v\n", arr, target, combinationSum(arr, target))

	arr, target = []int{3, 4, 5, 6}, 10
	fmt.Printf("The combinations of %v which sum up to %v are %v\n", arr, target, combinationSum(arr, target))
}
