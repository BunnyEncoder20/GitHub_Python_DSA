class Solution:
    def GCD(self, n1, n2):
        greatestDivisor = 1
        for i in range(1, min(n1, n2)):
            if n1 % i == 0 and n2 % i == 0:
                greatestDivisor = i
        return greatestDivisor


if __name__ == "__main__":
    print(Solution().GCD(4, 6))
