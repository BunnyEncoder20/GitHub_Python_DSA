from typing import List 

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0          # every instance should have a instance variable of count initialized to 0
        low = 0
        high = len(nums)-1
        
        self.mergeSort(nums,low,high)
        return self.count       # return the instance count
    
    def mergeSort(self,arr,low,high):
        
        if low>=high : return 
        
        mid = (low+high)//2
        
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.countPairs(arr,low,mid,high)
        
        self.merge(arr,low,mid,high)
    
    def countPairs(self,arr,low,mid,high):
        right = mid+1
        left = low
        while left <= mid :
            while right<=high and arr[left]>2*arr[right]:
                right+=1
            self.count += (right-(mid+1))               # keep adding the counts
            left+=1
    
    def merge(self, arr, low, mid, high):
        left = low
        right = mid+1
        temp = []
        
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        
        for i in range(low,high+1):
            arr[i] = temp[i-low]
            
        
        
    
if __name__ == "__main__":
    i = Solution()
    listNums = [[1,3,2,3,1],[2,4,3,5,1]]
    for nums in listNums : 
        print(i.reversePairs(nums))
        
    