class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # if not nums:
        #     if lower == upper:
        #         return [str(lower)]
        #     else:
        #         return [str(lower) + "->" + str(upper)]
        start = lower
        end = lower
        res = []
        for i in range(len(nums)):
            if nums[i] == end:
                start, end = nums[i] + 1, nums[i] + 1
                
            elif nums[i] > end:
                end = max(end, nums[i] - 1)
                
                if end != start:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start))
                    
                start, end = nums[i] + 1, nums[i] + 1
                
        if start < upper:       
            res.append(str(start) + "->" + str(upper))
        elif start == upper:
            res.append(str(start))
            
        return res         