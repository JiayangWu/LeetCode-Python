class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                # print nums1,nums2
                res.append(nums1[i])
                
            # print nums1,nums2,res
        return res