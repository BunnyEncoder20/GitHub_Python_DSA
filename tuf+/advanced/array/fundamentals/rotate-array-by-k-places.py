class Solution:
    def rotateArray(self, nums, k: int) -> None:
        length = len(nums)
        # find the actual k
        k %= length
        temp = [n for n in nums[:k]]

        for i in range(k, length):
            nums[i - k] = nums[i]

        for i in range(k):
            nums[length - k + i] = temp[i]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    Solution().rotateArray(nums, 2)
    print(nums)
    nums = [3, 4, 1, 5, 3, -5]
    Solution().rotateArray(nums, 8)
    print(nums)
