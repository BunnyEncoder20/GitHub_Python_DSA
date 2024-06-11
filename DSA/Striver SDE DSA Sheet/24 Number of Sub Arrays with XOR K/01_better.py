class Solution:
    def solve(self, nums, target):
        n = len(nums)
        counter = 0

        for i in range(n):
            xor = 0
            for j in range(i,n):
                xor = xor ^ nums[j]    
                if xor==target :
                    counter+=1
        return counter

if __name__ == "__main__":
    A1,A2 = [4, 2, 2, 6, 4],[5, 6, 7, 8, 9]
    B1,B2 = 6,5

    i = Solution()
    print(i.solve(A1,B1))
    print(i.solve(A2,B2))
