package main

import (
	"fmt"
	"slices"
	"sort"
)

func bruteThreeSum(nums []int) [][3]int {
	n := len(nums)
	set := make(map[[3]int]struct{})

	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if nums[i]+nums[j]+nums[k] == 0 {
					triplet := [3]int{nums[i], nums[j], nums[k]}

					// NOTE: When we make a slice of a array, we are actually making a pointer to the arr. That is why the original data is also mutated after the sorting of the slice
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

func optimalThreeSum(nums []int) [][]int {
	// we sort the nums
	sort.Ints(nums)

	// init the result
	res := [][]int{}

	// three (kinda like two) pointer loop
	n := len(nums)
	for i := range n - 2 {
		// avoiding dups
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}

		// two pointers init
		j, k := i+1, n-1

		for j < k {
			sum := nums[i] + nums[j] + nums[k]

			if sum < 0 {
				j++
			} else if sum > 0 {
				k--
			} else {
				// sum is 0; add it to the result
				res = append(res, []int{nums[i], nums[j], nums[k]})

				// updating pointers
				j++
				k--
				for nums[j] == nums[j-1] && j < k {
					j++
				}
				for nums[k] == nums[k+1] && j < k {
					k--
				}
			}
		}
	}

	return res
}

func main() {
	fmt.Println("Brute:")
	nums := []int{2, -2, 0, 3, -3, 5}

	// Call the threeSum
	ans1 := bruteThreeSum(nums)
	for _, triplet := range ans1 {
		fmt.Print("[")
		for _, num := range triplet {
			fmt.Printf("%d ", num)
		}
		fmt.Print("] ")
	}

	fmt.Println("\nOptimal:")
	nums = []int{2, -2, 0, 3, -3, 5}

	// Call the threeSum
	ans2 := optimalThreeSum(nums)
	for _, triplet := range ans2 {
		fmt.Print("[")
		for _, num := range triplet {
			fmt.Printf("%d ", num)
		}
		fmt.Print("] ")
	}

	fmt.Println()
}
