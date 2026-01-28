class Solution:
    def mergeSort(self, nums):
        low, high = 0, len(nums) - 1
        self.divide(nums, low, high)
        return nums

    def divide(self, nums, low, high):
        if low >= high:
            return

        # divide
        mid = (low + high) // 2
        self.divide(nums, low, mid)
        self.divide(nums, mid + 1, high)

        # and conquer
        self.merger(nums, low, mid, high)

    def merger(self, nums, low, mid, high):
        temp = []
        left, right = low, mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]


if __name__ == "__main__":
    print(Solution().mergeSort([7, 4, 1, 5, 3]))
    print(Solution().mergeSort([5, 4, 4, 1, 1]))
