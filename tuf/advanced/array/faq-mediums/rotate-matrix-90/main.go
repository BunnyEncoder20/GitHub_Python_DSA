package main

import "fmt"

func bruteRotateMatrix(arr [][]int) {
	// init the matrix
	n := len(arr)
	res := make([][]int, n)
	for row := range n {
		res[row] = make([]int, n)
	}

	for i := range n {
		for j := range n {
			res[j][n-1-i] = arr[i][j]
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			arr[i][j] = res[i][j]
		}
	}
}

func optimalRotateMatrix(arr [][]int) {
	// init
	n := len(arr)

	// making a transpose of the mat
	for i := range n {
		for j := range i {
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
		}
	}

	// reversing each row of mat
	for row := range n {
		for l, r := 0, n-1; l < r; l, r = l+1, r-1 {
			arr[row][l], arr[row][r] = arr[row][r], arr[row][l]
		}
	}
}

func main() {
	arr := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	// bruteRotateMatrix(arr)
	optimalRotateMatrix(arr)
	fmt.Println("Rotated Matrix1:")
	for row := range len(arr) {
		for col := range len(arr[0]) {
			fmt.Print(arr[row][col], " ")
		}
		fmt.Println()
	}

	arr = [][]int{
		{0, 1, 1, 2},
		{2, 0, 3, 1},
		{4, 5, 0, 5},
		{4, 6, 7, 0},
	}

	// bruteRotateMatrix(arr)
	optimalRotateMatrix(arr)
	fmt.Println("Rotated Matrix2:")
	for row := range len(arr) {
		for col := range len(arr[0]) {
			fmt.Print(arr[row][col], " ")
		}
		fmt.Println()
	}

	arr = [][]int{
		{1, 1, 2},
		{5, 3, 1},
		{5, 3, 5},
	}

	// bruteRotateMatrix(arr)
	optimalRotateMatrix(arr)
	fmt.Println("Rotated Matrix3:")
	for row := range len(arr) {
		for col := range len(arr[0]) {
			fmt.Print(arr[row][col], " ")
		}
		fmt.Println()
	}
}
