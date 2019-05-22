class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        p1 = 0
        p2 = 0
        while(p1 < m and p2 < n):
            if (nums1[p1] <= nums2[p2]):
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1
        
        while(p1 < m):
            temp.append(nums1[p1])
            p1 += 1
        while(p2 < n):
            temp.append(nums2[p2])
            p2 += 1
        
        for i in range(0, m + n ):
            nums1[i] = temp[i]
        
        # return nums1
        