class Solution:
    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isPrime(13))  # True
