package main

import "fmt"

func bruteMedian(arr1 []int, arr2 []int) float64 {
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

func betterMedian(arr1 []int, arr2 []int) float64 {
	len1, len2 := len(arr1), len(arr2)

	// calc the indexs for median
	idx1, idx2 := ((len1+len2)/2)-1, (len1+len2)/2
	ele1, ele2 := -1, -1
	counter := 0

	// make the pointers
	i, j := 0, 0
	for i < len1 && j < len2 {
		if arr1[i] <= arr2[j] {
			if counter == idx1 {
				ele1 = arr1[i]
			}
			if counter == idx2 {
				ele2 = arr1[i]
			}
			counter++
			i++
		} else {
			if counter == idx1 {
				ele1 = arr2[j]
			}
			if counter == idx2 {
				ele2 = arr2[j]
			}
			counter++
			j++
		}
	}

	// if some elements are left in the other arr
	for i < len1 {
		if counter == idx1 {
			ele1 = arr1[i]
		}
		if counter == idx2 {
			ele2 = arr1[i]
		}
		counter++
		i++
	}
	for j < len2 {
		if counter == idx1 {
			ele1 = arr2[j]
		}
		if counter == idx2 {
			ele2 = arr2[j]
		}
		counter++
		j++
	}

	if (len1+len2)%2 == 1 {
		return float64(ele2)
	} else {
		return float64(ele1+ele2) / 2.0
	}
}

func main() {
	arr1, arr2 := []int{2, 4, 6}, []int{1, 3, 5}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, bruteMedian(arr1, arr2))
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, betterMedian(arr1, arr2))
	arr1, arr2 = []int{2, 4, 6}, []int{1, 3}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, bruteMedian(arr1, arr2))
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, betterMedian(arr1, arr2))
	arr1, arr2 = []int{2, 4, 5}, []int{1, 6}
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, bruteMedian(arr1, arr2))
	fmt.Printf("The median of arays %v & %v is %.2f\n", arr1, arr2, betterMedian(arr1, arr2))
}
