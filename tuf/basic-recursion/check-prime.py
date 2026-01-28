class Solution:
    def checkPrime(self, num):
        if num <= 1:
            return False
        return self.recursiveFunc(2, num)

    def recursiveFunc(self, i, n):
        # base case
        if i == n:
            return True

        if n % i == 0:
            return False

        return self.recursiveFunc(i + 1, n)


if __name__ == "__main__":
    print(Solution().checkPrime(5))
    print(Solution().checkPrime(15))
    print(Solution().checkPrime(41))
