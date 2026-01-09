class Solution:
    def reverseNumber(self, n):
        num = n
        reversedNumber = 0

        while num:
            lastdigit = num % 10
            reversedNumber = reversedNumber * 10 + lastdigit
            num //= 10

        return reversedNumber


if __name__ == "__main__":
    print(Solution().reverseNumber(12345))
