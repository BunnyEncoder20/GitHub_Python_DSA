class Solution:
    def mostFrequent(self, nums: list, n: int) -> int:
        fpp = {}
        maxfreq = 1
        maxElement = nums[0]
        for num in nums:
            if fpp.get(num):
                fpp[num] += 1
            else:
                fpp[num] = 1
        for key, freq in fpp.items():
            if freq > maxfreq:
                maxfreq = freq
                maxElement = key
            elif freq == maxfreq:
                maxElement = min(key, maxElement)
        return maxElement


if __name__ == "__main__":
    print(Solution().mostFrequent([2, 3, 2, 5, 8, 2, 3], 7))  # 2
