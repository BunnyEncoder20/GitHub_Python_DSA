class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums) - 1):
            min_idx = i

            # SELECTING the minimum element in the unsorted part of the array
            for j in range(i, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j

            # Swap the min_idx with the ith idx
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return


if __name__ == "__main__":
    nums = [64, 25, 12, 22, 11]
    Solution().selectionSort(nums)
    print(nums)  # [11, 12, 22, 25, 64]
