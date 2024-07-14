from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        nums2_nge = {}
        ans = []
        stack = []

        for i in range(n2-1,-1,-1):
            if not stack:
                nums2_nge[nums2[i]] = -1
                stack.append(nums2[i])
            elif stack and stack[-1] > nums2[i]:
                nums2_nge[nums2[i]] = stack[-1]
                stack.append(nums2[i])
            elif stack and stack[-1]<=nums2[i]:
                while stack and stack[-1]<=nums2[i]:
                    stack.pop()
                if stack:
                    nums2_nge[nums2[i]] = stack[-1]
                    stack.append(nums2[i])
                else:
                    nums2_nge[nums2[i]] = -1
                    stack.append(nums2[i])
        
        ans = [nums2_nge[n] for n in nums1]
        
        return ans

if __name__ == '__main__':
    nums1 = [4,2,1]
    nums2 = [1,3,4,2]
    res = Solution().nextGreaterElement(nums1,nums2)
    print(*res) # -1 3 -1