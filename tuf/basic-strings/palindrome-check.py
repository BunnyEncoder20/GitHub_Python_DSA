class Solutin:
    def checkPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True


if __name__ == "__main__":
    print(Solutin().checkPalindrome("aabbccbbaa"))
