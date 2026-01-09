class Solution:
    def countOddDigits(self, n):
        # trivial case
        if n == 0:
            return 1

        count = 0
        num = n

        while num:
            if (num % 10) % 2 != 0:
                count += 1
            num = num // 10

        return count


if __name__ == "__main__":
    print(Solution().countOddDigits(12345))
