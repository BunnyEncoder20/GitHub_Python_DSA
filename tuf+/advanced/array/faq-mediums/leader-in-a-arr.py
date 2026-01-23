class Solution:
    def bruteLeaderElements(self, nums):
        n = len(nums)
        ans = []

        for i in range(n - 1):
            isLeader = True
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    isLeader = False
                    break
            if isLeader:
                ans.append(nums[i])

        ans.append(nums[-1])
        return ans

    def optimalLeaderElements(self, nums):
        # trivial case
        if not nums:
            return

        lastLeader = nums[-1]
        ans = [nums[-1]]
        n = len(nums)

        for i in range(n - 2, -1, -1):
            if nums[i] > lastLeader:
                lastLeader = nums[i]
                ans.append(nums[i])

        ans.reverse()
        return ans


if __name__ == "__main__":
    print(Solution().bruteLeaderElements([1, 2, 5, 3, 1, 2]))
    print(Solution().bruteLeaderElements([-3, 4, 5, 1, -4, -5]))
    print(Solution().optimalLeaderElements([1, 2, 5, 3, 1, 2]))
    print(Solution().optimalLeaderElements([-3, 4, 5, 1, -4, -5]))
