package main

import (
	"fmt"
	"slices"
)

func aggressiveCows(nums []int, k int) int {
	slices.Sort(nums)
	maxMinimumDistance := 0
	for distance := 1; distance < slices.Max(nums); distance++ {
		if canPlace(nums, distance, k) {
			maxMinimumDistance = distance
			continue
		} else {
			return maxMinimumDistance
		}
	}
	return maxMinimumDistance
}

func canPlace(positions []int, minDistance int, numCows int) bool {
	// At the start, we always place the first cow at first available positions
	countPlaced, lastPlacedAt := 1, positions[0]

	for i := 1; i < len(positions); i++ {
		// try to place cow at this pos
		if positions[i]-lastPlacedAt >= minDistance {
			lastPlacedAt = positions[i]
			countPlaced++
			// probably could just return true from here,
			// as soon as countPlaced == numCows
		}
	}

	if countPlaced >= numCows {
		return true // we were able to place all cows while maintaining minDistance
	} else {
		return false // we were not able to place all the cows for the distance given
	}
}

func main() {
	k, nums := 4, []int{0, 3, 4, 7, 10, 9} // 3
	fmt.Printf("The maximum possible minimum distance for positions %v between any two cows will be %d\n", nums, aggressiveCows(nums, k))
	k, nums = 2, []int{4, 2, 1, 3, 6} // 5
	fmt.Printf("The maximum possible minimum distance for positions %v between any two cows will be %d\n", nums, aggressiveCows(nums, k))
	k, nums = 3, []int{10, 1, 2, 7, 5} //
	fmt.Printf("The maximum possible minimum distance for positions %v between any two cows will be %d\n", nums, aggressiveCows(nums, k))
}
