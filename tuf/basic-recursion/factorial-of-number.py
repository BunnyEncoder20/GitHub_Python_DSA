class Solution:
    def factorial(self, n) -> int:
        # base case: smaller than 1 cause the n could be just 0
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    print(Solution().factorial(5))
    print(Solution().factorial(3))
