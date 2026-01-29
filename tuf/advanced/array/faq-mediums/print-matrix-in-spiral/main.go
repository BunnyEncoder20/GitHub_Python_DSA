package main

import "fmt"

func spiralOrder(mat [][]int) []int {
	// Trivial case
	if len(mat) == 0 {
		return []int{}
	}

	// init
	rows, cols := len(mat), len(mat[0])
	result := []int{}

	top, left := 0, 0
	right, bottom := cols-1, rows-1

	for top <= bottom && left <= right {
		// moving left to right
		for j := left; j <= right; j++ {
			result = append(result, mat[top][j])
		}
		top++ // moving the top

		// moving top to bottom on the right side
		for i := top; i <= bottom; i++ {
			result = append(result, mat[i][right])
		}
		right-- // moving the right

		if top <= bottom {
			for j := right; j >= left; j-- {
				result = append(result, mat[bottom][j])
			}
			bottom-- // moving bottom
		}

		if left <= right {
			for i := bottom; i >= top; i-- {
				result = append(result, mat[i][left])
			}
			left++ // moving the left
		}
	}

	return result
}

func main() {
	mat1 := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println(spiralOrder(mat1))

	mat2 := [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}}
	fmt.Println(spiralOrder(mat2))

	mat3 := [][]int{{1, 2}, {3, 4}, {5, 6}, {7, 8}}
	fmt.Println(spiralOrder(mat3))
}
