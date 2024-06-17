# Optimal Solution : Kadane's Algorithm
# Time Complexity : O(n)
# Space Complexity : O(1) [in-place modification]

def maximum_subArray(nums):
    maxSum = float('-inf')
    currSum = 0
    start,end = 0,0
    
    
    for i in range(0, len(nums)):
        if currSum == 0:
            start = i
        
        currSum += nums[i]

        if maxSum < currSum:
            maxSum = currSum
            end = i
        
        if currSum < 0:
            currSum = 0
    
    print("MaxSum : ", maxSum)
    print("MaxSubArray : ", nums[start:end+1])

if __name__ == '__main__':
    nums = [-2, -5, 6, -2, -3, 1, 5, -6]
    maximum_subArray(nums)