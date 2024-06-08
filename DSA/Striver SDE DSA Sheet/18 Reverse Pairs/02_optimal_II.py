# Same algo but with no global variable 

from typing import List 

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        
        return self.mergeSort(nums,low,high)        # return the count which is sent back from the algo
        
    
    def mergeSort(self,arr,low,high):
        count = 0                                   # one count for this function to return
        if low>=high : return 0
        
        mid = (low+high)//2
        
        count += self.mergeSort(arr,low,mid)
        count += self.mergeSort(arr,mid+1,high)
        count += self.countPairs(arr,low,mid,high)
        
        self.merge(arr,low,mid,high)
        
        return count
    
    def countPairs(self,arr,low,mid,high):
        right = mid+1
        left = low
        count = 0                                  # one count for this function to return
        
        while left <= mid :
            while right<=high and arr[left]>2*arr[right]:
                right+=1
            count += (right-(mid+1))
            left+=1

        return count
    
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
        
    