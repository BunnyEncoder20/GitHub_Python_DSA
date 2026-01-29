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

func pascalTriangles(r, c int) int {
	return nCr(r-1, c-1)
}

func main() {
	fmt.Println(pascalTriangles(4, 2))
	fmt.Println(pascalTriangles(5, 3))
	fmt.Println(pascalTriangles(6, 2))
}
