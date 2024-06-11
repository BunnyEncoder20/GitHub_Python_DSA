from collections import defaultdict

class Solution:
    def solve(self, nums, target):
        n = len(nums)
        counter = 0
        xor = 0
        hashmap = defaultdict(int) # defaultdict used because if the key is not present it'll return 0 by default
        hashmap[0]=1    # setting the first value

        for i in range(n):
            xor = xor ^ nums[i]
            required = xor^target

            counter += hashmap[required]  # if element in hashmap will return count of that else 0
            hashmap[xor]+=1

        return counter

if __name__ == "__main__":
    A1,A2 = [4, 2, 2, 6, 4],[5, 6, 7, 8, 9]
    B1,B2 = 6,5

    i = Solution()
    print(i.solve(A1,B1))
    print(i.solve(A2,B2))
