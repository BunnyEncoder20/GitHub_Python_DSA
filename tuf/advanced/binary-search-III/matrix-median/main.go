package main

import (
	"fmt"
	"math"
	"slices"
)

// TC: nxm + nxm.log(nxm)
func findMedian(mat [][]int) int {
	rows, cols := len(mat), len(mat[0])
	n := rows * cols
	matSlice := make([]int, 0, n)

	for i := range rows {
		for j := range cols {
			matSlice = append(matSlice, mat[i][j])
		}
	}

	// sort the slices
	slices.Sort(matSlice)

	// return median
	if n%2 == 0 {
		return (matSlice[n/2] + matSlice[n/2-1]) / 2
	} else {
		return matSlice[n/2]
	}
}

func optimalFindMedian(matrix [][]int) int {
	rows, cols := len(matrix), len(matrix[0])
	n := rows * cols
	reqOnLeft := n / 2 // median always has n/2 elements to it's left

	low, high := getLowAndHigh(matrix, rows, cols)
	for low <= high {
		mid := low + (high-low)/2
		numOfLessThanEqual := getLessThanEqual(matrix, mid)

		if numOfLessThanEqual > reqOnLeft {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return low
}

func getLowAndHigh(matrix [][]int, rows int, cols int) (int, int) {
	low, high := math.MaxInt, math.MinInt
	for i := range rows {
		low = min(low, matrix[i][0])
		high = max(high, matrix[i][cols-1])
	}
	return low, high
}

func getLessThanEqual(matrix [][]int, target int) int {
	lessThanEqualCount := 0
	for i := range len(matrix) {
		lessThanEqualCount += getUpperBound(matrix[i], target)
	}
	return lessThanEqualCount
}

func getUpperBound(arr []int, target int) int {
	low, high := 0, len(arr)-1
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] > target {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return low
}

func main() {
	mat := [][]int{{1, 4, 9}, {2, 5, 6}, {3, 7, 8}}
	fmt.Printf("Median for matric %v is %d\n", mat, findMedian(mat))
	fmt.Printf("Median for matric %v is %d\n", mat, optimalFindMedian(mat))

	mat = [][]int{{1, 3, 8}, {2, 3, 4}, {1, 2, 5}}
	fmt.Printf("Median for matric %v is %d\n", mat, findMedian(mat))
	fmt.Printf("Median for matric %v is %d\n", mat, optimalFindMedian(mat))

	mat = [][]int{{1, 4, 15}, {2, 5, 6}, {3, 8, 11}}
	fmt.Printf("Median for matric %v is %d\n", mat, findMedian(mat))
	fmt.Printf("Median for matric %v is %d\n", mat, optimalFindMedian(mat))
}
