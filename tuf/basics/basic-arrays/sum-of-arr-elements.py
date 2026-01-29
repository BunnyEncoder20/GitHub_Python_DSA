class Solution:
    def sumOfArrayElements(self, arr):
        summ = 0
        for n in arr:
            summ += n
        return summ


if __name__ == "__main__":
    print(Solution().sumOfArrayElements([1, 2, 3, 4, 5]))  # Output: 15
