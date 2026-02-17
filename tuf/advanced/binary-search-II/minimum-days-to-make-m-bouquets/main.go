package main

import (
	"fmt"
	"slices"
)

func getMinimumDays(totalRoses int, rosesBloomsOn []int, requiredBouquets int, rosesPerBouquet int) int {
	// edge case: if all rosesBloomed and still less that requiredBouquets x rosesPerBouquet
	// this is an impossible case
	if rosesPerBouquet*requiredBouquets > totalRoses {
		return -1
	}

	// min and max of the rosesBloomsOn array are the boundaries of our search
	minDay, maxDay := slices.Min(rosesBloomsOn), slices.Max(rosesBloomsOn)

	for day := minDay; day <= maxDay; day++ {
		if bouquets := howManyBouquets(rosesBloomsOn, day, rosesPerBouquet); bouquets >= requiredBouquets {
			return day
		}
	}

	return -1 // just backup
}

func optimalGetMinimumDays(n int, nums []int, m int, k int) int {
	// edge case
	if k*m > n {
		return -1
	}

	// cause the fn(day) = numBouquet > m is an monotonic increase func,
	// we can run binary search on this shiz
	low, high := slices.Min(nums), slices.Max(nums)

	for low <= high {
		mid := low + (high-low)/2 // to prevent int overflow
		numBouquet := howManyBouquets(nums, mid, k)
		if numBouquet >= m {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return low // when to not send this
}

func howManyBouquets(rosesBloomsOn []int, day int, rosesPerBouquet int) int {
	numBouquet, counter := 0, 0

	for _, dayOfBlooming := range rosesBloomsOn {
		if day >= dayOfBlooming {
			counter += 1
		} else {
			numBouquet += counter / rosesPerBouquet // count the num of bouquets
			counter = 0                             // reset counter
		}
	}
	// adding the last counter reading to numBouquet
	numBouquet += counter / rosesPerBouquet

	// fmt.Printf("on day %d we can make %d bouquets\n", day, numBouquet)
	return numBouquet
}

func main() {
	n, nums, m, k := 8, []int{7, 7, 7, 7, 13, 11, 12, 7}, 2, 3 // 12
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, getMinimumDays(n, nums, m, k))
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, optimalGetMinimumDays(n, nums, m, k))
	n, nums, m, k = 5, []int{1, 10, 3, 10, 2}, 3, 2 // -1
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, getMinimumDays(n, nums, m, k))
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, optimalGetMinimumDays(n, nums, m, k))
	n, nums, m, k = 5, []int{1, 10, 3, 10, 2}, 3, 1
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, getMinimumDays(n, nums, m, k))
	fmt.Printf("Minimum number of days needed to make %d bouquets is %d\n", m, optimalGetMinimumDays(n, nums, m, k))
}
