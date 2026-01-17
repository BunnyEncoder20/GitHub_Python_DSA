class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums) - 1, -1, -1):
            for j in range(0, i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                print(nums)  # Debug: Print the array after each swap
        return nums


if __name__ == "__main__":
    print(
        Solution().bubbleSort([64, 34, 25, 12, 22, 11, 90])
    )  # [11, 12, 22, 25, 34, 64, 90]
