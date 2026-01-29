class Solution:
    def NnumbersSum(self, N) -> int:
        # base case
        if N == 0:
            return 0

        # normally
        else:
            return N + self.NnumbersSum(N - 1)


if __name__ == "__main__":
    print(Solution().NnumbersSum(2))
    print(Solution().NnumbersSum(4))
    print(Solution().NnumbersSum(10))
