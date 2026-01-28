class Solution:
    def quickSort(self, nums):
        self.qs(nums, 0, len(nums) - 1)
        return nums

    def qs(self, nums, low, high):
        # base conditions
        if low >= high:
            return

        # Normally
        partisionIndex = self.getPartisionIndex(nums, low, high)
        self.qs(nums, low, partisionIndex - 1)
        self.qs(nums, partisionIndex + 1, high)

    def getPartisionIndex(self, nums, low, high) -> int:
        pivot = nums[low]
        i, j = low, high

        # Find the swapping indexing
        while i < j:
            # finds first element which is greater than the pivot
            while nums[i] <= pivot and i < high:
                i += 1
            # finds first element which is smaller than the pivot
            while nums[j] > pivot and j > low:
                j -= 1
            # swap the elements
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        # j would be at the place where the pivot should be
        nums[j], nums[low] = nums[low], nums[j]
        return j


if __name__ == "__main__":
    print(Solution().quickSort([7, 4, 1, 5, 3]))
    print(Solution().quickSort([3, 6, 8, 10, 1, 2, 1]))
    print(Solution().quickSort([1, 2, 3, 4, 5]))
