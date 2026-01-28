class Solution:
    def bruteUnionArray(self, nums1, nums2):
        result = set(n for n in nums1 + nums2)
        return list(result)

    def optimalUnionArray(self, nums1, nums2):
        union = [None]
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if nums1[i] != union[-1]:
                    union.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                if nums1[i] != union[-1]:
                    union.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                if nums2[j] != union[-1]:
                    union.append(nums2[j])
                j += 1

        while i < len(nums1):
            if union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1
        while j < len(nums2):
            if union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        union.pop(0)
        return union


if __name__ == "__main__":
    print(Solution().bruteUnionArray([1, 2, 3, 4, 5], [1, 2, 7]))
    print(Solution().bruteUnionArray([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))
    print(Solution().optimalUnionArray([1, 2, 3, 4, 5], [1, 2, 7]))
    print(Solution().optimalUnionArray([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))
