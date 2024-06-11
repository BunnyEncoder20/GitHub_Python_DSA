class Solution:
    def maxLen(self, n, arr):
        target = n
        n = len(arr)
        hashmap = {}
        summation = 0
        longest = 0

        for i in range(n) : 
            summation+=arr[i]
            if summation == target : 
                length = i+1
                longest = max(longest,length)
            
            required = summation - target
            if required in hashmap : 
                length = i - hashmap[required]
                longest = max(longest,length)
            
            if summation not in hashmap : 
                hashmap[summation] = i    # import, do not update the sum for a newer index, as we need the longest, Hence the left most index 

        return longest

if __name__ == "__main__":
    i = Solution()
    n,arr=8,[15,-2,2,-8,1,7,10,23]
    print(i.maxLen(n,arr))