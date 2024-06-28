class Solution:
    def getPermutation(self,n:int,k:int)->int:
        fact = 1 
        nums = []
        for i in range(1,n):
            nums.append(i)
            fact *= i
        nums.append(n)
        k-=1            # Cause we using 0 based indexing
        ans = ""
        while True:
            ans+=str(nums[k//fact])     # select the right digit
            nums.pop(k//fact)           # remove that digit from the list of available digits
            if not nums : break         # Stop if nums becomes empty 

            # update the k and fact
            k %= fact
            fact = fact//len(nums)
        return ans
    
if __name__ == "__main__":
    n = 4
    k = 17
    ans = Solution().getPermutation(n, k)
    print("The Kth permutation sequence is", ans)