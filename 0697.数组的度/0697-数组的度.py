class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 计算数组的degree
        # 2. 找到哪些元素出现了degree次
        # 3. 利用2中元素第一次出现的下标和最后一次出现的下标来计算对应子数组的长度
        degree = 0
        for digit in set(nums):
            degree = max(degree, nums.count(digit))
            
        candidates = list()
        for digit in set(nums):
            if nums.count(digit) == degree:
                candidates.append(digit)
                
        l = len(nums)
        reversenums = nums[::-1]
        res = l
        for candidate in candidates:
            left_pos = nums.index(candidate)
            right_pos = l - reversenums.index(candidate)

            res = min(res, right_pos - left_pos)
            
        return res