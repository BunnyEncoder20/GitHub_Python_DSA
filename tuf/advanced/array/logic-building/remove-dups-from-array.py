from typing import List


class Solution:
    def bruteRemoveDuplicates(self, nums: List[int]) -> int:
        # set does not store dups. Sort the unique elements
        tempSet = sorted(set(nums))
        for i in range(len(tempSet)):
            nums[i] = tempSet[i]

        return len(tempSet)

    def optimalRemoveDuplicates(self, nums: List[int]) -> int:
        lastUnique = 0
        for j in range(len(nums)):
            if nums[j] != nums[lastUnique]:
                lastUnique += 1
                nums[lastUnique] = nums[j]
        return lastUnique + 1


if __name__ == "__main__":
    print(Solution().bruteRemoveDuplicates([0, 0, 3, 3, 5, 6]))
    print(Solution().bruteRemoveDuplicates([-2, 2, 4, 4, 4, 4, 5, 5]))

    print(Solution().optimalRemoveDuplicates([0, 0, 3, 3, 5, 6]))
    print(Solution().optimalRemoveDuplicates([-2, 2, 4, 4, 4, 4, 5, 5]))
