class Solution:
    def reverseArrayNaive(self, arr: list, n: int) -> list:
        revarr = [None] * n
        for i in range(n):
            revarr[i] = arr[n - 1 - i]
        for i in range(n):
            arr[i] = revarr[i]
        return arr

    def reverseArrayOptimal(self, arr: list, n: int) -> list:
        i, j = 0, n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
        return arr


if __name__ == "__main__":
    print(Solution().reverseArrayNaive([1, 2, 3, 4, 5], 5))  # [5, 4, 3, 2, 1]
    print(Solution().reverseArrayOptimal([1, 2, 3, 4, 5], 5))  # [5, 4, 3, 2, 1]
