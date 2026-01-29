class Solution:
    def palindromeCheck(self, s):
        return self.recursiveFunc(s, 0, len(s) - 1)

    def recursiveFunc(self, str, i, j):
        # base case:
        if i >= j:
            return True

        if str[i] != str[j]:
            return False

        return self.recursiveFunc(str, i + 1, j - 1)


if __name__ == "__main__":
    print(Solution().palindromeCheck("hannah"))
    print(Solution().palindromeCheck("aabbaA"))
    print(Solution().palindromeCheck("aabbaA"))
