class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        
        res = []
        for key, val in dic1.items():
            res += [key] * min(val, dic2[key])
        return res