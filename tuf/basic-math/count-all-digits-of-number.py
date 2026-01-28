class Solution:
    def countDigits(self, n):
        # trivial case
        if n == 0:
            return 1

        count = 0
        num = n
        while num:
            count += 1
            num = num // 10

        return count


if __name__ == "__main__":
    print(Solution().countDigits(12345))
