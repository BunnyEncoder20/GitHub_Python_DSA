# Brute Slution for Merging 2 Sorted arrays 
# Time Complexity : O(n+m)
# Space Complexity: O(n+m)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = []
        left,right = 0,0

        while left<m and right<n :
            if nums1[left] < nums2[right]:
                ans.append(nums1[left])
                left+=1
            else : 
                ans.append(nums2[right])
                right+=1
        
        ans.extend([nums1[i] for i in range(left,m)])
        ans.extend([nums2[i] for i in range(right,n)])

        return ans



if __name__ == "__main__":
    ins = Solution()
    list_of_nums1 = [[1,2,3],[2,5,6]]
    list_of_nums2 = [[1],[]]
    list_of_nums3 = [[],[1]]

    print(ins.merge(list_of_nums1[0],len(list_of_nums1[0]),list_of_nums1[1],len(list_of_nums1[1])))
    print(ins.merge(list_of_nums2[0],len(list_of_nums2[0]),list_of_nums2[1],len(list_of_nums2[1])))
    print(ins.merge(list_of_nums3[0],len(list_of_nums3[0]),list_of_nums3[1],len(list_of_nums3[1])))
    
    