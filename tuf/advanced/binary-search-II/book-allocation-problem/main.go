package main

import (
	"fmt"
)

func findPages(pagesInBook []int, numStudents int) int {
	// edge case number of students more than number of books
	n := len(pagesInBook)
	if n < numStudents {
		return -1
	}

	// we should start biggest page size of the array
	// so that every student can hold all the books in the array
	// max pages someone can hold will obviously be the total pages in the entire array
	minPages, maxPages := getTotalSumAndMax(pagesInBook)

	for pages := minPages; pages <= maxPages; pages++ {
		if countStudents(pagesInBook, pages) <= numStudents {
			return pages
		}
	}

	return -1 // fallback
}

func optimalFindPages(pagesInBook []int, numStudents int) int {
	// edge case: there are not enough books
	if len(pagesInBook) < numStudents {
		return -1
	}

	// cause this is another monotonic func, we can apply binary search
	low, high := getTotalSumAndMax(pagesInBook)

	for low <= high {
		mid := low + (high-low)/2
		if countStudents(pagesInBook, mid) <= numStudents {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return low // we are looking for first true
}

func getTotalSumAndMax(pages []int) (int, int) {
	total, maxPages := 0, -1<<63
	for _, pages := range pages {
		total += pages
		if pages > maxPages {
			maxPages = pages
		}
	}
	return maxPages, total
}

func countStudents(pagesInBook []int, pageLimit int) int {
	reqStudents, currentlyHolding := 1, 0

	for i := range pagesInBook {
		if currentlyHolding+pagesInBook[i] <= pageLimit {
			currentlyHolding += pagesInBook[i]
		} else {
			reqStudents++
			currentlyHolding = pagesInBook[i]
		}
	}

	return reqStudents
}

func main() {
	pages, m := []int{12, 34, 67, 90}, 2
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, findPages(pages, m))
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, optimalFindPages(pages, m))
	pages, m = []int{25, 46, 28, 49, 24}, 4
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, findPages(pages, m))
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, optimalFindPages(pages, m))
	pages, m = []int{15, 17, 20}, 2
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, findPages(pages, m))
	fmt.Printf("For books with pages %v and %d children, at max one child will have %d pages\n", pages, m, optimalFindPages(pages, m))
}
