class Soluton:
    def largestElement(self, nums):
        largestElement = nums[0]
        for num in nums:
            if largestElement < num:
                largestElement = num
        return largestElement


if __name__ == "__main__":
    print(Soluton().largestElement([7, 4, 1, 5, 3]))  # Output: 7
    print(Soluton().largestElement([3, 6, 8, 10, 1, 2, 1]))  # Output: 10
    print(Soluton().largestElement([1, 2, 3, 4, 5]))  # Output: 5
