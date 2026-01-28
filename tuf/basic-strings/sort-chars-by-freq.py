class Solution:
    def frequencySort(self, s):
        fpp = {}
        for ch in s:
            fpp[ch] = fpp.get(ch, 0) + 1

        sortedKeyValTuples = sorted(
            fpp.items(), key=lambda keyVal: (-keyVal[1], keyVal[0])
        )

        return [ch for ch, _ in sortedKeyValTuples]


if __name__ == "__main__":
    print(Solution().frequencySort("raaaajj"))
    print(Solution().frequencySort("tree"))
