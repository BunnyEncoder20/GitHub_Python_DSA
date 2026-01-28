class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(6))
