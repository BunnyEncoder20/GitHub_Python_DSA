class Solution:
    def largestOddNum(self, s):
        lastOddDigitIndex = None
        for i in range(len(s) - 1, -1, -1):
            if (int(s[i])) % 2 != 0:
                lastOddDigitIndex = i
                break

        # There is no odd digit
        if lastOddDigitIndex is None:
            return ""

        firstNonZeroDigitIndex = 0
        for i in range(len(s)):
            if s[i] != "0":
                firstNonZeroDigitIndex = i
                break

        return s[firstNonZeroDigitIndex : lastOddDigitIndex + 1]


if __name__ == "__main__":
    print(Solution().largestOddNum("5347"))
