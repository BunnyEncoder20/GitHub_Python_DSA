class Solution:
    def secondLargestElement(self, nums):
        largest, secondLargestElement = float("-inf"), float("-inf")
        for num in nums:
            if num > largest:
                secondLargestElement = largest
                largest = num
            elif num > secondLargestElement and num != largest:
                secondLargestElement = num
        return secondLargestElement if secondLargestElement != float("-inf") else -1


if __name__ == "__main__":
    print(Solution().secondLargestElement([3, 5, 2, 4, 1]))  # Output: 4
    print(Solution().secondLargestElement([10, 20, 20, 30]))  # Output: 20
    print(Solution().secondLargestElement([1, 1, 1]))  # Output: -1
