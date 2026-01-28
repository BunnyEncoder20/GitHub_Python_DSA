class Solution:
    def countPrimes(self, n: int) -> int:
        start, end = 2, n + 1
        count = 0
        for i in range(start, end):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    print(Solution().countPrimes(10))  # Expected output: 4
