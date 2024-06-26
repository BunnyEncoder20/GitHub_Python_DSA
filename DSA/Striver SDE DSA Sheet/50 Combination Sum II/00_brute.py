def combinationSum2(nums,target):
    n = len(nums)
    ds = []
    answer = set()
    nums.sort()         # for sorted creation of combinations

    def combinationSum2Helper(index,target):
        if index==n:
            if target==0:
                answer.add(tuple(ds[:]))
            return 
        if nums[index]<=target:
            ds.append(nums[index])
            combinationSum2Helper(index+1,target-nums[index])
            ds.pop()
        combinationSum2Helper(index+1,target)
    
    combinationSum2Helper(0,target)
    answer = [list(combo) for combo in answer]
    return answer

if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    comb = combinationSum2(v, 8)
    print(comb)