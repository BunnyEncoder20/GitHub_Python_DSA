class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        summ = 0

        for i in range(1, n // 2 + 1):
            if n % i == 0:
                summ += i

        return summ == n


if __name__ == "__main__":
    print(Solution().checkPerfectNumber(28))  # True
