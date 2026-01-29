package main

import "fmt"

func nCr(n, r int) int {
	// tivial case
	if r == 1 {
		return n
	}

	// select the smaller of r or n-r for less iterations
	if r > n-r {
		r = n - r
	}

	// init result
	result := 1

	for i := 0; i < r; i++ {
		result = result * (n - i) / (i + 1)
	}

	return result
}

func pascalTriangles1(r, c int) int {
	return nCr(r-1, c-1)
}

func pascalTriangles2(row int) []int {
	res := make([]int, row)
	if row > 0 {
		res[0] = 1 // first and last element of each row is always 1
	}

	for col := 1; col < row; col++ {
		res[col] = (res[col-1] * (row - col)) / (col)
	}

	return res
}

func main() {
	fmt.Println("Pascal Triangles 1:")
	fmt.Println(pascalTriangles1(4, 2))
	fmt.Println(pascalTriangles1(5, 3))
	fmt.Println(pascalTriangles1(6, 2))

	fmt.Println("\nPascal Triangles 2:")
	fmt.Println(pascalTriangles2(4))
	fmt.Println(pascalTriangles2(5))
	fmt.Println(pascalTriangles2(6))

	fmt.Println("\nPascal Triangles 3:")
}
