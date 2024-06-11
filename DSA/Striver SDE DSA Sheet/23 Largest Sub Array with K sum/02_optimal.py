class Solution:
    def maxLen(self, target, arr):
        n = len(arr)
        front,back = 0,0
        current_sum = 0
        longest = 0

        while front<n : 
            # add the current element to sum
            current_sum += arr[front]

            # if the sum > target, move the back pointer
            while current_sum > target : 
                current_sum -= arr[back]
                back+=1
            
            # if the sum = target
            if current_sum == target:
                longest = max(longest,front-back+1)
            
            # if the sum < target, move the front pointer
            front += 1

        return longest 
    
if __name__ == "__main__":
    i = Solution()
    n,arr=3,[1,2,3,1,1,1,1]
    print(i.maxLen(n,arr))