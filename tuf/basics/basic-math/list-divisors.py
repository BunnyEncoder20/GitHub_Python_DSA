class Solution:
    def divisors(self, n):
        ans = []
        for i in range(1, n + 1):
            if n % i == 0:
                ans.append(i)
        return ans


if __name__ == "__main__":
    print(Solution().divisors(12))  # Output: [1, 2, 3, 4, 6, 12]
