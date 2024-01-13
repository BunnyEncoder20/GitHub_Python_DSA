def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr1 = [0]*m
        arr2 = [0]*n

        for i in range(0,m):
            arr1[i] = nums1[i]
        for i in range(0,n):
            arr2[i] = nums2[i]
        
        print(arr1)
        print(arr2)
        print(sorted(arr1+arr2))
        
        # Note how we assign the new arrray : 
        nums1[:m+n] = sorted(arr1 + arr2)

merge(nums1=[1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)