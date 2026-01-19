class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().linearSearch([7, 4, 1, 5, 3], 5))  # Output: 3
    print(Solution().linearSearch([3, 6, 8, 10, 1, 2, 1], 10))  # Output: 3
    print(Solution().linearSearch([1, 2, 3, 4, 5], 6))  # Output: -1
