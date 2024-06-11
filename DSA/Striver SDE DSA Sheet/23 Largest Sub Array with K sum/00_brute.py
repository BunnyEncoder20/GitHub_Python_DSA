class Solution:
    def maxLen(self, n, arr):
        target = n 
        n = len(arr)
        longest = 0

        # Generating all the sub array
        for i in range(n):
            for j in range(i+1,n):
                subarray = arr[i:j+1]
                total = sum(subarray)

                if total==target :
                    longest = max(longest,(j-i+1)) 
        
        return longest


if __name__ == "__main__":
    i = Solution()
    n,arr=8,[15,-2,2,-8,1,7,10,23]
    print(i.maxLen(n,arr))