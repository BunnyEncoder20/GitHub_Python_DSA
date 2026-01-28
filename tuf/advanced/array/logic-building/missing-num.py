class Solution:
    def missingNumber1(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumber2(self, nums):
        # making a freq hashmap
        fpp = {n: 0 for n in range(len(nums) + 1)}
        for n in nums:
            fpp[n] += 1

        for val, freq in fpp.items():
            if freq == 0:
                return val

        return -1

    def optimalMissingNumbers(self, nums):
        n = len(nums)

        # Using maths
        arrSum = sum(nums)
        nSum = n * (n + 1) // 2  # formula for sum of n natural numbers

        # missing number is the only one not added in the arrSum but is there in nSum
        return nSum - arrSum


if __name__ == "__main__":
    print(Solution().missingNumber1([0, 2, 3, 1, 4]))
    print(Solution().missingNumber1([0, 1, 2, 4, 5, 6]))

    print(Solution().missingNumber2([0, 2, 3, 1, 4]))
    print(Solution().missingNumber2([0, 1, 2, 4, 5, 6]))

    print(Solution().optimalMissingNumbers([0, 2, 3, 1, 4]))
    print(Solution().optimalMissingNumbers([0, 1, 2, 4, 5, 6]))
