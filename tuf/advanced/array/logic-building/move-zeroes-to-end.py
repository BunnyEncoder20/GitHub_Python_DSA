class Solution:
    def bruteMoveZeroes(self, nums):
        # copy over the non zero elements first
        temp = [n for n in nums if n != 0]

        # Copy over the non zero elements to the start of the array
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Make the remaining elements zero
        for i in range(len(temp), len(nums)):
            nums[i] = 0

        return nums

    def optimalMoveZeroes(self, nums):
        j = 0  # points to where the non zero element should be placed

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums


if __name__ == "__main__":
    print(Solution().bruteMoveZeroes([0, 1, 4, 0, 5, 2]))
    print(Solution().bruteMoveZeroes([0, 0, 0, 1, 3, -2]))

    print(Solution().optimalMoveZeroes([0, 1, 4, 0, 5, 2]))
    print(Solution().optimalMoveZeroes([0, 0, 0, 1, 3, -2]))
