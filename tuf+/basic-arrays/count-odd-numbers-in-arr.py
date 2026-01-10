class Solution:
    def countOddNumbers(self, arr) -> int:
        count = 0
        for n in arr:
            if n % 2 != 0:
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().countOddNumbers([1, 2, 3, 4, 5]))  # Output: 3
