class Solution:
    def bruteRearrangeArray(self, nums):
        posi, negi = [], []
        for n in nums:
            if 0 < n:
                posi.append(n)
            else:
                negi.append(n)

        ans = [None] * len(nums)
        for i in range(len(nums) // 2):
            ans[2 * i] = posi[i]
            ans[2 * i + 1] = negi[i]

        return ans

    def optimalRearrangeArray(self, nums):
        posIndex, negIndex = 0, 1
        ans = [None] * len(nums)

        for n in nums:
            if n > 0:
                ans[posIndex] = n
                posIndex += 2
            else:
                ans[negIndex] = n
                negIndex += 2

        return ans


if __name__ == "__main__":
    print(Solution().bruteRearrangeArray([2, 4, 5, -1, -3, -4]))
    print(Solution().bruteRearrangeArray([1, -1, -3, -4, 2, 3]))
    print(Solution().optimalRearrangeArray([2, 4, 5, -1, -3, -4]))
    print(Solution().optimalRearrangeArray([1, -1, -3, -4, 2, 3]))
