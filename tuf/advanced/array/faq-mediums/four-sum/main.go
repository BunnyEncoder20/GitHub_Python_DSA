package main

import (
	"fmt"
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	// init
	n := len(nums)
	resMap := make(map[[4]int]struct{})

	// sorting the nums
	sort.Ints(nums)

	// four pointers logic
	for i := 0; i < n-3; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}

		for j := i + 1; j < n-2; j++ {
			if j != i+1 && nums[j] == nums[j-1] {
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
					resMap[[4]int{nums[i], nums[j], nums[k], nums[l]}] = struct{}{}
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

	res := make([][]int, 0, len(resMap))
	for quad := range resMap {
		temp := []int{quad[0], quad[1], quad[2], quad[3]}
		res = append(res, temp)
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

	nums = []int{1, 1, 3, 4, -3}
	fmt.Println("")
	ans = fourSum(nums, 5)
	for _, quads := range ans {
		fmt.Printf("%v", quads)
	}
}
