package main

import (
	"fmt"
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
