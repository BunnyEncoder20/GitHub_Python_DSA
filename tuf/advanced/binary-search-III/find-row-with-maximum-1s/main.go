package main

import (
	"fmt"
	"math"
)

func rowWithMax1s(mat [][]int) int {
	maxOnes, maxOnesRow := math.MinInt, -1
	rows, cols := len(mat), len(mat[0])

	for i := range rows {
		countOnes := 0
		for j := range cols {
			if mat[i][j] == 1 {
				countOnes++
				if countOnes > maxOnes {
					maxOnes = countOnes
					maxOnesRow = i
				}
			}
		}
	}

	return maxOnesRow
}

func betterRowWithMax1s(mat [][]int) int {
	// cause rows are sorted, we could just find the first one
	// If we found 1 at j then, for n cols, the num of 1s would be n-j
	maxOnes, maxOnesRow := math.MinInt, -1
	rows, cols := len(mat), len(mat[0])

	for i := range rows {
		for j := range cols {
			// linear search for first 1
			if mat[i][j] == 1 {
				countOnes := cols - j
				if countOnes > maxOnes {
					maxOnes = countOnes
					maxOnesRow = i
				}
			}
		}
	}

	return maxOnesRow
}

func optimalRowWithMax1s(mat [][]int) int {
	// cause the rows are sorted, we can binary search the rows
	// for the first 1 and then just use that to get the count of 1s for that row
	rows, cols := len(mat), len(mat[0])
	maxOnes, maxOnesRow := 0, -1

	for i := range rows {
		low, high := 0, cols-1

		for low <= high {
			mid := low + (high-low)/2
			if mat[i][mid] == 0 {
				low = mid + 1
			}
			if mat[i][mid] == 1 {
				high = mid - 1
			}
		}
		// in the end, low should be at the first one
		countOnes := cols - low
		if countOnes == 0 {
			continue
		} else if countOnes > maxOnes {
			maxOnes = countOnes
			maxOnesRow = i
		}
	}

	return maxOnesRow
}

func main() {
	mat := [][]int{{1, 1, 1}, {0, 0, 1}, {0, 0, 0}}
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, rowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, betterRowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, optimalRowWithMax1s(mat))

	mat = [][]int{{0, 0}, {0, 0}}
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, rowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, betterRowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, optimalRowWithMax1s(mat))

	mat = [][]int{{0, 0, 1}, {0, 1, 1}, {0, 1, 1}}
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, rowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, betterRowWithMax1s(mat))
	fmt.Printf("The row with maximum number of 1's in %v is %d\n", mat, optimalRowWithMax1s(mat))
}
