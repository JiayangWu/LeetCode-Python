class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        start, end = nums[0], nums[0]
        
        res = list()
        for i, x in enumerate(nums):
            if i == 0:
                continue
            
            if x == end + 1:#代表连续
                end = x
            elif x != end + 1: #中断了 或者是最后一个数了
                # print i, x, start, end
                temp = ""
                if start == end: #只有一个数
                    temp += str(end)
                else:
                    temp += str(start) + "->" + str(end)
                res.append(temp)
                
                start, end = x, x
                
            if i == len(nums) - 1:
                temp = ""
                if start == end: #只有一个数
                    temp += str(end)
                else:
                    temp += str(start) + "->" + str(end)
                res.append(temp)     
                
        # print start, end
        return res if len(nums) > 1 else [str(nums[0])]
            