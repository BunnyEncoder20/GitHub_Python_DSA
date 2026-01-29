class Solution:
    def reverseArray(self, nums):
        return self.recursiveFunc(nums, 0, len(nums) - 1)

    def recursiveFunc(self, nums, i, j):
        # base case
        if i >= j:
            return nums

        # swap the numbers
        nums[i], nums[j] = nums[j], nums[i]

        return self.recursiveFunc(nums, i + 1, j - 1)


if __name__ == "__main__":
    print(Solution().reverseArray([1, 2, 3, 4, 5]))
    print(Solution().reverseArray([1, 3, 3, 3, 5]))
