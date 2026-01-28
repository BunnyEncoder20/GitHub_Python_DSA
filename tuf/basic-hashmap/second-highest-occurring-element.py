class Solution:
    def secondHighest(self, nums):
        fpp = {}
        for n in nums:
            if fpp.get(n):
                fpp[n] += 1
            else:
                fpp[n] = 1

        maxfreq, maxElement = -1, -1
        secondMaxFreq, secondMaxElement = -1, -1

        for num, freq in fpp.items():
            if freq > maxfreq:
                secondMaxFreq, secondMaxElement = maxfreq, maxElement
                maxfreq, maxElement = freq, num
            elif freq == maxfreq:
                maxElement = min(num, maxElement)
            elif freq > secondMaxFreq:
                secondMaxFreq, secondMaxElement = freq, num
            elif freq == secondMaxFreq:
                secondMaxElement = min(num, secondMaxElement)
        return secondMaxElement


if __name__ == "__main__":
    print(Solution().secondHighest([1, 2, 2, 3, 3, 3]))  # 2
