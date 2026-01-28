class Solution:
    def reverseString1(self, s):
        return self.recursiveFunc1(s, 0)

    def recursiveFunc1(self, s, i):
        # base case
        if i == len(s):
            return []
        else:
            subList = self.recursiveFunc1(s, i + 1)
            subList.append(s[i])
            return subList

    def reverseString2(self, s):
        return self.recursiveFunc2(s, 0, len(s) - 1)

    def recursiveFunc2(self, s, i, j):
        # base case
        if i >= j:
            return s

        s[i], s[j] = s[j], s[i]
        return self.recursiveFunc2(s, i + 1, j - 1)


if __name__ == "__main__":
    print(Solution().reverseString1(["h", "e", "l", "l", "o"]))
    print(Solution().reverseString2(["b", "y", "e"]))
