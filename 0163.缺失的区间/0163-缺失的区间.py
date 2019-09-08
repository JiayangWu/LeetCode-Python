class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        start, end = lower, lower #左闭右开
        res = []
        for i, num in enumerate(nums):
            if num == end: #连上了
                start, end = num + 1, num + 1
            elif num > end: #没连上
                end = max(end, num - 1)
                if end - start == 0: #只有一个数
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start, end = num + 1, num + 1
        end = upper
        if start < end:
            res.append(str(start) + "->" + str(end))
        elif end == start: #只有一个数
                res.append(str(start))
        return res
                    
                