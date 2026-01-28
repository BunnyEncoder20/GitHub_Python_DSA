class Solution:
    def leftRotateArrayByOne(self, nums):
        temp = nums[0]

        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[len(nums) - 1] = temp

        return nums


if __name__ == "__main__":
    print(
        Solution().leftRotateArrayByOne([1, 2, 3, 4, 5])
    )  # Expected output: [5, 1, 2, 3, 4]
    print(
        Solution().leftRotateArrayByOne([10, 20, 30])
    )  # Expected output: [20, 30, 10]
    print(Solution().leftRotateArrayByOne([7]))  # Expected output: [7]
