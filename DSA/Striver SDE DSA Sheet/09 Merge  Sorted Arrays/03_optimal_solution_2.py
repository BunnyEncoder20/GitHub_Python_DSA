# Optimal solution 2 for Merging 2 Sorted Arrays with constant space 
# uses GAP method from Shell Sorting method.
# Time Complexity : 
# Space Complexity : 


from typing import List 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = [nums2[i] for i in range (n)]
        length = m+n
        gap = (length//2)+(length%2)  # eas way of getting the ceil value after divind even or odd number

        while gap>0 : 
            left = 0
            right = left+gap

            while right<length:
                if nums1[left] < nums1[right] :
                    left+=1
                    right+=1
                    continue
                else :
                    nums1[left],nums1[right]=nums1[right],nums1[left]
                    left+=1
                    right+=1
                    
            if gap == 1 : break
            gap = (gap//2)+(gap%2)


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