class Solution:
    def isSorted(self, nums):
        if len(nums) <= 1:
            return True

        return self.recursive(nums, 0)

    def recursive(self, nums, i):
        # base case
        if i + 1 == len(nums):
            return True

        if nums[i] > nums[i + 1]:
            return False

        return self.recursive(nums, i + 1)


if __name__ == "__main__":
    print(Solution().isSorted([1, 2, 3, 4, 5]))
    print(Solution().isSorted([1, 2, 1, 4, 5]))
