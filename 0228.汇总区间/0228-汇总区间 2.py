class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        start, end = nums[0], nums[0]
        res = []
        for i, num in enumerate(nums):
            if i != 0:
                if num == end + 1:
                    end += 1
                else:
                    if end - start == 0:
                        res.append(str(end))
                    else:
                        res.append(str(start) + "->" + str(end))
                    start, end = num, num
        if end - start == 0:
            res.append(str(end))
        else:
            res.append(str(start) + "->" + str(end))
        return res