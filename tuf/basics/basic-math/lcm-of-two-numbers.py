class Solution:
    def LCM(self, n1, n2) -> int:
        multiple = max(
            n1, n2
        )  # any number smaller than the larger number cannot be the LCM (cause then it wouldn't be a multiple of the larger number)

        while True:
            if multiple % n1 == 0 and multiple % n2 == 0:
                return multiple
            multiple += max(
                n1, n2
            )  # we don't need to check every number, only the multiples of the larger number


if __name__ == "__main__":
    print(Solution().LCM(4, 6))
