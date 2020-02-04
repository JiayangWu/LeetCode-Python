class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping = dict()
        
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                top = stack.pop()
                mapping[top] = num
            stack.append(num)

        res = []
        for num in nums1:
            if num in mapping:
                res.append(mapping[num])
            else:
                res.append(-1)
                
        return res