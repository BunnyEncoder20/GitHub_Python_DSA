import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        # handling the zero case here
        if n == 0:
            return True

        # The power should be the length of the digits
        power = self.countDigits(n)
        sum = 0
        num = n

        while num:
            sum += (num % 10) ** power
            num //= 10

        return sum == n

    def countDigits(self, n: int) -> int:
        if n == 0:
            return 1
        return int(math.log10(n)) + 1


if __name__ == "__main__":
    print(Solution().isArmstrong(153))  # True
