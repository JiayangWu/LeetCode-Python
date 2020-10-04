class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        while p1 < len(nums1):
            res.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            res.append(nums2[p2])
            p2 += 1
        print res
        return res[len(res) // 2] if len(res) % 2 == 1 else (res[len(res) // 2 - 1] + res[len(res) // 2]) * 1.0 / 2