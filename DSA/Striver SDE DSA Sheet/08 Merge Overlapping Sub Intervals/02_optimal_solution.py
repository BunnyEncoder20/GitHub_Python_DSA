# Optimal Solution for Sub interval Overlapping 
# Time Complexity : O(nlogn) + O(n) [sorting + for loops]
# Space Complexity :  O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []

        for i in range(n):

            # Check if we need to make a new ans interval
            if not ans or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])

            # Check if the interval is overlapping with previous ans interval
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])

        return ans


if __name__ == '__main__':
    ins = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]        
    intervals2 = [[1,4],[4,5]]
    print(ins.merge(intervals1))
    print(ins.merge(intervals2))