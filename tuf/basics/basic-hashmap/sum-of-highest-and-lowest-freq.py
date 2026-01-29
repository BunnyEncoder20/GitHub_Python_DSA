from typing import List


class Solution:
    def sumHighestAndLowestFreq(self, nums: List):
        fpp = {}
        for num in nums:
            fpp[num] = fpp.get(num, 0) + 1
        highestFreq = max(fpp.values())
        lowestFreq = min(fpp.values())
        return highestFreq + lowestFreq


if __name__ == "__main__":
    print(Solution().sumHighestAndLowestFreq([1, 2, 2, 3, 3, 3]))
    print(Solution().sumHighestAndLowestFreq([10, 9, 7, 7, 8, 8, 8]))
