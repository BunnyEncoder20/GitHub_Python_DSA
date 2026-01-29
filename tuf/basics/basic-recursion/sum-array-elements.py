class Solution:
    def arraySum(self, nums):
        return self.recursiveFunc(nums, 0)

    def recursiveFunc(self, arr, i):
        if i == len(arr):
            return 0
        else:
            return arr[i] + self.recursiveFunc(arr, i + 1)


if __name__ == "__main__":
    print(Solution().arraySum([1, 2, 3]))
    print(Solution().arraySum([5, 8, 1]))
    print(Solution().arraySum([12, 9, 17]))
