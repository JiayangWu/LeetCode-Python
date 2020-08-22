class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dups = set(nums1) & set(nums2)

        s1 = self.getFragmentedSum(nums1, dups)
        s2 = self.getFragmentedSum(nums2, dups)

        res = 0
        for sum1, sum2 in zip(s1, s2):
            res += max(sum1, sum2)
        return res % (10 ** 9 + 7)

    def getFragmentedSum(self, nums, dups):
        l = []
        s = 0
        for num in nums:
            s += num 
            if num in dups:
                l.append(s)
                s = 0
        l.append(s)
        return l