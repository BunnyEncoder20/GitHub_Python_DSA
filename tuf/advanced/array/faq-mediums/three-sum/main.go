package main

import (
	"fmt"
	"slices"
)

func threeSum(nums []int) [][3]int {
	n := len(nums)
	set := make(map[[3]int]struct{})

	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if nums[i]+nums[j]+nums[k] == 0 {
					triplet := [3]int{nums[i], nums[j], nums[k]}
					slices.Sort(triplet[:])
					set[triplet] = struct{}{}
				}
			}
		}
	}

	res := [][3]int{}
	for key := range set {
		res = append(res, key)
	}

	return res
}

func main() {
	nums := []int{2, -2, 0, 3, -3, 5}

	// Call the threeSum
	ans := threeSum(nums)
	for _, triplet := range ans {
		fmt.Print("[")
		for _, num := range triplet {
			fmt.Printf("%d ", num)
		}
		fmt.Print("] ")
	}

	fmt.Println()
}
