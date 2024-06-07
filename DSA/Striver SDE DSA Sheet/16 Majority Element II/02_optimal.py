from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1,counter2 = 0,0
        element1,element2 = None,None 
        n = len(nums)

        for i in range(n):
            if counter1==0 and nums[i] != element2:
                element1 = nums[i]
                counter1 = 1
            elif counter2==0 and nums[i] != element1:
                element2 = nums[i]
                counter2 = 1
            elif nums[i]==element1 : counter1+=1
            elif nums[i]==element2 : counter2+=1
            else:
                counter1-=1
                counter2-=1
        
        # After the above loop we will have some number in element1 and element2, but cannot say for sure they are the mojority elements (in case there might not be any majority elements)
        # Hence we need to verify 
        count1,count2=0,0
        ans = []
        for num in nums:
            if num == element1 : count1+=1
            if num == element2 : count2+=1 
        if count1>n//3 : ans.append(element1)
        if count2>n//3 : ans.append(element2)
        
        ans.sort() 
        return ans


if __name__ == "__main__":
    listNums = [[3,2,3],[1],[1,2]]
    i = Solution()
    for num in listNums:
        print(i.majorityElement(num))
    