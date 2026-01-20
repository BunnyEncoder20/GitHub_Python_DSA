class Solution:
    def moveZeroes(self, nums):
        # copy over the non zero elements first
        temp = [n for n in nums if n != 0]

        # Copy over the non zero elements to the start of the array
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Make the remaining elements zero
        for i in range(len(temp), len(nums)):
            nums[i] = 0

        return nums


if __name__ == "__main__":
    print(Solution().moveZeroes([0, 1, 4, 0, 5, 2]))
    print(Solution().moveZeroes([0, 0, 0, 1, 3, -2]))
