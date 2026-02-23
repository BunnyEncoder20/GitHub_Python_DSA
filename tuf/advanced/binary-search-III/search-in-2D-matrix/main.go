package main

import "fmt"

func searchMatrix(mat [][]int, target int) bool {
	rows, cols := len(mat), len(mat[0])
	for i := range rows {
		for j := range cols {
			if mat[i][j] == target {
				return true
			}
		}
	}
	return false
}

func betterSearchMatrix(mat [][]int, target int) bool {
	// cause the rows are sorted,
	// we could identify if the target lies within that row by checking it's boundaries
	rows, cols := len(mat), len(mat[0])
	for i := range rows {
		if target < mat[i][0] || mat[i][cols-1] < target {
			continue
		}

		// target might lie within this row
		for j := range cols {
			if mat[i][j] == target {
				return true
			}
		}
	}
	return false
}

func optimalSearchMatrix(mat [][]int, target int) bool {
	// cause the rows are all sorted and the next row first element will always be more
	// than the previous rows last element, we can treat the 2D matrix as a 1D sorted array
	// Hence we can binary search for the the target
	// idx i will correcspond to the 2D coords: [i/m, i%m]
	rows, cols := len(mat), len(mat[0])
	low, high := 0, rows*cols-1

	for low <= high {
		mid := low + (high-low)/2
		row, col := mid/cols, mid%cols
		if mat[row][col] == target {
			return true
		} else if mat[row][col] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return false
}

func main() {
	mat, target := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}, 8
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, searchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, betterSearchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, optimalSearchMatrix(mat, target))

	mat, target = [][]int{{1, 2, 4}, {6, 7, 8}, {9, 10, 34}}, 78
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, searchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, betterSearchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, optimalSearchMatrix(mat, target))

	mat, target = [][]int{{1, 2, 4}, {6, 7, 8}, {9, 10, 34}}, 7
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, searchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, betterSearchMatrix(mat, target))
	fmt.Printf("Does target:%d exists within the matrix %v ? %v\n", target, mat, optimalSearchMatrix(mat, target))
}
