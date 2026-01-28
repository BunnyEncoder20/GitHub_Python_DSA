class Solution:
    def addDigits(self, num):
        # base case
        if num < 10:
            return num

        digit_sum = self.summationOfCurrentDigits(num)

        return self.addDigits(digit_sum)

    def summationOfCurrentDigits(self, num):
        if num == 0:
            return 0
        else:
            return self.summationOfCurrentDigits(num // 10) + (num % 10)


if __name__ == "__main__":
    print(Solution().addDigits(529))
    print(Solution().addDigits(101))
