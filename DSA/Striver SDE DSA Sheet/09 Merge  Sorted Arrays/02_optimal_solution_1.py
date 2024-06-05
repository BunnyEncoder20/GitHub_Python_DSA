# Optimal solution 1 for Merging 2 Sorted Arrays with constant space 
# Time Complexity : O(min(n,m)) + O(nlogn) + O(mlogm)
# Space Complexity : O(1)


from typing import List 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left,right = n-1,0

        while left>=0 and right<m:
            if(nums1[left]>=nums2[right]):
                nums1[left],nums2[right]=nums2[right],nums1[left]
                left-=1
                right+=1
            else:
                break
        
        nums1.sort()
        nums2.sort()


if __name__ == "__main__":
    ins = Solution()
    list_of_nums1 = [[1,2,3],[2,5,6]]
    list_of_nums2 = [[1],[]]
    list_of_nums3 = [[],[1]]

    ins.merge(list_of_nums1[0],len(list_of_nums1[0]),list_of_nums1[1],len(list_of_nums1[1]))
    ins.merge(list_of_nums2[0],len(list_of_nums2[0]),list_of_nums2[1],len(list_of_nums2[1]))
    ins.merge(list_of_nums3[0],len(list_of_nums3[0]),list_of_nums3[1],len(list_of_nums3[1]))
    
    print(list_of_nums1[0], end=' ')
    print(list_of_nums1[1])
    print(list_of_nums2[0], end=' ')
    print(list_of_nums2[1])
    print(list_of_nums3[0], end=' ')
    print(list_of_nums3[1])


