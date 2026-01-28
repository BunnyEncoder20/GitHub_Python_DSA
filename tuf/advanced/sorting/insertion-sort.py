class Solution:
    def insertionSort(self, nums):
        for i in range(len(nums)):
            for j in range(i, -1, -1):
                if j - 1 >= 0 and nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return nums


if __name__ == "__main__":
    print(Solution().insertionSort([7, 4, 1, 5, 3]))
    print(Solution().insertionSort([5, 4, 4, 1, 1]))
