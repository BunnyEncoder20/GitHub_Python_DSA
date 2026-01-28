class Solution:
    def isSorted(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isSorted([1, 2, 2, 3, 4]))  # True
