package main

import "fmt"

func median(arr1 []int, arr2 []int) float64 {
	l1, l2 := len(arr1), len(arr2)
	l3 := l1 + l2
	arr3 := make([]int, 0, l3)

	// merging both arrs
	i, j := 0, 0
	for i < l1 && j < l2 {
		if arr1[i] <= arr2[j] {
			arr3 = append(arr3, arr1[i])
			i++
		} else {
			arr3 = append(arr3, arr2[j])
			j++
		}
	}

	// if some elements are left in the other arr...
	for i < l1 {
		arr3 = append(arr3, arr1[i])
		i++
	}
	for j < l2 {
		arr3 = append(arr3, arr2[j])
		j++
	}

	// calculate median
	if l3%2 == 1 {
		return float64(arr3[l3/2]) // mid number is median in odd no. of elements
	} else {
		return (float64(arr3[l3/2]) + float64(arr3[l3/2-1])) / 2.0
	}
}

func main() {
	arr1, arr2 := []int{2, 4, 6}, []int{1, 3, 5}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, median(arr1, arr2))
	arr1, arr2 = []int{2, 4, 6}, []int{1, 3}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, median(arr1, arr2))
	arr1, arr2 = []int{2, 4, 5}, []int{1, 6}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, median(arr1, arr2))
}
