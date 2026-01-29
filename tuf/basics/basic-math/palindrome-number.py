class Solution:
    def isPalindrome(self, n):
        num = n
        revnum = self.reverseNumber(n)
        return num == revnum

    def reverseNumber(self, n):
        reversedNumber = 0
        while n:
            reversedNumber = (reversedNumber * 10) + (n % 10)
            n //= 10
        return reversedNumber


if __name__ == "__main__":
    print(Solution().isPalindrome(1001))
