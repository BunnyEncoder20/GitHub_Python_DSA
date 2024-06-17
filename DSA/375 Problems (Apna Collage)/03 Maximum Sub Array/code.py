def getMaxSubArray(nums):
    
    if(len(nums)==1):
        return nums,nums[0]
    
    maxSum = float('-inf')
    start,summation=0,0
    maxSubArray = []
    
    for i in range(len(nums)):
        summation += nums[i]
        
        if summation > maxSum:
            maxSum = summation
            maxSubArray = nums[start:i+1]
        
        if summation < 0:
            summation = 0
            start = i+1
    
    return maxSubArray,maxSum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [5,4,-1,7,8]
    maxSubArray, maxSum = getMaxSubArray(nums)
    print(f"The subarray {maxSubArray} has the largest sum {maxSum}.")