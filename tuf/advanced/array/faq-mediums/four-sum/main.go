package main

import (
	"fmt"
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	// init
	n := len(nums)
	res := [][]int{}

	// sorting the nums
	sort.Ints(nums)

	// four pointers logic
	for i := 0; i < n-3; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}

		for j := i + 1; j < n-2; j++ {
			if j != 0 && nums[j] == nums[j-1] {
				continue
			}

			// init the 2 pointers
			k, l := j+1, n-1

			for k < l {
				sum := nums[i] + nums[j] + nums[k] + nums[l]

				if sum < target {
					k++
				} else if sum > target {
					l--
				} else {
					// sum is equal to target
					res = append(res, []int{nums[i], nums[j], nums[k], nums[l]})
					k++
					l--
					for nums[k] == nums[k-1] && k < l {
						k++
					}
					for nums[l] == nums[l+1] && k < l {
						l--
					}
				}
			}
		}
	}
	return res
}

func main() {
	nums := []int{1, -2, 3, 5, 7, 9}
	ans := fourSum(nums, 7)
	fmt.Println("Quadruplets:")
	for _, quads := range ans {
		fmt.Printf("%v ", quads)
	}

	nums = []int{7, -7, 1, 2, 14, 3}
	fmt.Println("")
	ans = fourSum(nums, 9)
	for _, quads := range ans {
		fmt.Printf("%v", quads)
	}
}
