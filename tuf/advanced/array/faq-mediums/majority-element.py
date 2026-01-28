from typing import List


class Solution:
    def bruteMajorityElement(self, nums: List[int]) -> int | None:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count > len(nums) // 2:
                return nums[i]
        return

    def betterMajorityElement(self, nums: List[int]) -> int | None:
        # making a frequency map
        fpp = {}
        for n in nums:
            fpp[n] = fpp.get(n, 0) + 1

        for n, freq in fpp.items():
            if freq > len(nums) // 2:
                return n

        return

    def optimalMajorityElement(self, nums: List[int]) -> int | None:
        element, count = 0, 0

        for n in nums:
            if count == 0:
                element = n
                count = 1
            elif n == element:
                count += 1
            else:
                count -= 1

        if nums.count(element) > len(nums) // 2:
            return element
        else:
            return


if __name__ == "__main__":
    print(Solution().bruteMajorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))  # 7
    print(Solution().bruteMajorityElement([1, 1, 1, 2, 1, 2]))  # 1
    print(Solution().bruteMajorityElement([-1, -1, -1, -1]))  # -1
    print(Solution().betterMajorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))  # 7
    print(Solution().betterMajorityElement([1, 1, 1, 2, 1, 2]))  # 1
    print(Solution().betterMajorityElement([-1, -1, -1, -1]))  # -1
    print(Solution().optimalMajorityElement([7, 0, 0, 1, 7, 7, 2, 7, 7]))  # 7
    print(Solution().optimalMajorityElement([1, 1, 1, 2, 1, 2]))  # 1
    print(Solution().optimalMajorityElement([-1, -1, -1, -1]))  # -1
