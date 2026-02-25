package main

import "fmt"

// Brute and  better same as the prevous question
// For this the "sorted array" is the from 0 to col-1 and then col-1 to row-1
// hence we can binary search that shiz
func searchMatrix(matrix [][]int, target int) bool {
	rows, cols := len(matrix), len(matrix[0])
	i, j := 0, cols-1
	for i <= rows-1 && j >= 0 {
		if matrix[i][j] == target {
			return true
		} else if matrix[i][j] < target {
			// if the current < target, increase value: go down
			i++
		} else {
			// if the current > target, decrease value: go left
			j--
		}
	}
	return false
}

func main() {
	matrix, target := [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}, 5
	fmt.Printf("Is the target:%d present in %v matrix ? %v\n", target, matrix, searchMatrix(matrix, target))

	matrix, target = [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}, 20
	fmt.Printf("Is the target:%d present in %v matrix ? %v\n", target, matrix, searchMatrix(matrix, target))

	matrix, target = [][]int{{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}}, 1
	fmt.Printf("Is the target:%d present in %v matrix ? %v\n", target, matrix, searchMatrix(matrix, target))
}
