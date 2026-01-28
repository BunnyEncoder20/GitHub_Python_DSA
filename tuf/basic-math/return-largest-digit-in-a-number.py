class Solution:
    def largestDigit(self, n):
        num = n
        largestDigit = 0

        while num:
            digit = num % 10
            if digit > largestDigit:
                largestDigit = digit
            num //= 10

        return largestDigit


if __name__ == "__main__":
    print(Solution().largestDigit(29))  # Output: 9
