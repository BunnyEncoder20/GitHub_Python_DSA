from typing import List


class Solution:
    def reverseString(self, s: List):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return s


if __name__ == "__main__":
    print(Solution().reverseString(["h", "e", "l", "l", "o"]))
