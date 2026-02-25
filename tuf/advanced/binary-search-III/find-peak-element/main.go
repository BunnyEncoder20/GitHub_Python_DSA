package main

import (
	"fmt"
)

func linearFindPeakElement(arr []int) int {
	n := len(arr)

	// trivial case
	if n == 1 {
		return 0
	}

	for i := range len(arr) {
		switch {
		case i == 0:
			if arr[i] > arr[i+1] {
				return i
			}
		case i == len(arr)-1:
			if arr[i] > arr[i-1] {
				return i
			}
		case arr[i-1] < arr[i] && arr[i] > arr[i+1]:
			return i
		}
	}
	return -1
}

func binaryFindPeakElement(arr []int) int {
	// check edge cases
	n := len(arr)
	if n == 1 || arr[0] > arr[1] {
		return 0
	}
	if arr[n-2] < arr[n-1] {
		return n - 1
	}

	low, high := 1, n-2
	for low <= high {
		mid := low + (high-low)/2

		if arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1] {
			return mid
		}

		if arr[mid] < arr[mid+1] {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1 // dummy return
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 5, 1}
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, linearFindPeakElement(arr))
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, binaryFindPeakElement(arr))

	arr = []int{1, 2, 1, 3, 5, 6, 4}
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, linearFindPeakElement(arr))
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, binaryFindPeakElement(arr))

	arr = []int{-2, -1, 3, 4, 5}
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, linearFindPeakElement(arr))
	fmt.Printf("The peak elemetns of %v is at idx: %d\n", arr, binaryFindPeakElement(arr))
}
