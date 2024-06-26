def combinationSum2(nums,target):
    answer = []
    ds = []
    nums.sort()

    def combinationHelper(index,target):
        if target==0: 
            answer.append(ds[:])
            return 
        
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            if nums[i]>target:
                break
            ds.append(nums[i])
            combinationHelper(i+1,target-nums[i])
            ds.pop()
    
    combinationHelper(0,target)
    return answer

if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(comb)