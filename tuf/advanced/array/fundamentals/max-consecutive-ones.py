class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count, maxCount = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(count, maxCount)
            if num != 1:
                count = 0

        return maxCount


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # Output: 2
    print(Solution().findMaxConsecutiveOnes([0, 0, 0]))  # Output: 0
