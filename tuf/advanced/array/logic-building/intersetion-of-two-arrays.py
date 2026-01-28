class Solution:
    def bruteIntersectionArrays(self, nums1, nums2):
        visited = [0] * len(nums2)
        intersection = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and not visited[j]:
                    intersection.append(nums2[j])
                    visited[j] = 1
                elif nums2[j] > nums1[i]:
                    break

        return intersection

    def optimalIntersectionArrays(self, nums1, nums2):
        i, j = 0, 0
        intersection = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1

        return intersection


if __name__ == "__main__":
    print(Solution().bruteIntersectionArrays([1, 2, 2, 3, 5], [1, 2, 7]))
    print(Solution().bruteIntersectionArrays([1, 2, 2, 3, 3, 3], [2, 3, 3, 4, 5, 7]))
    print(Solution().optimalIntersectionArrays([1, 2, 2, 3, 5], [1, 2, 7]))
    print(Solution().optimalIntersectionArrays([1, 2, 2, 3, 3, 3], [2, 3, 3, 4, 5, 7]))
