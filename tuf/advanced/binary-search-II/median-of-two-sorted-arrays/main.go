package main

import (
	"fmt"
	"math"
)

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

func optimalMedian(arr1 []int, arr2 []int) float64 {
	// NOTE: This is based on valid symmetry: we try to contruct the 2 halfs of the combines array
	// by selecting some number of elements from both array. There will be only one such config
	// which would yield a sorted result. We Binary search that config.
	// Median we will get from the greates element on the left and least element on the right. (at least for even  elements)
	len1, len2 := len(arr1), len(arr2)
	total := len1 + len2
	leftSideNeeded := (total + 1) / 2
	low, high := 0, min(len1, len2)

	for low <= high {
		// mid1 -> I want these many from arr1 on left side
		// mid2 -> I want these many from arr2 on let side
		mid1 := low + (high-low)/2
		mid2 := leftSideNeeded - mid1

		// assign the correct values to the 4 boundary values
		left1, left2 := math.MinInt, math.MinInt
		right1, right2 := math.MaxInt, math.MaxInt
		if mid1 > 0 {
			left1 = arr1[mid1-1]
		}
		if mid2 > 0 {
			left2 = arr2[mid2-1]
		}
		if mid1 < len1 {
			right1 = arr1[mid1]
		}
		if mid2 < len2 {
			right2 = arr2[mid2]
		}

		// base condition
		if left1 < right2 && left2 < right1 {
			if total%2 == 0 {
				return float64(max(left1, left2)+min(right1, right2)) / 2.0
			} else {
				return float64(max(left1, left2))
			}
		}

		// go left: more elements of arr1 have been considered than needed
		// we need to reduce the number of elements of arr1 (take mid towards low)
		if left1 > right2 {
			high = mid1 - 1
		}

		// go right: more eleements of arr2 have been considered thatn needed,
		// we need to use more of arr1 elements: take mid to high value
		if left2 > right1 {
			low = mid1 + 1
		}
	}

	return -1.0 // should never reach
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
