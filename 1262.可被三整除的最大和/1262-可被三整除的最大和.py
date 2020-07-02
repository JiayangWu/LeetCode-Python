class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(list)
        
        nums.sort()
        for num in nums:
            dic[num % 3].append(num)
        
            
        s = sum(nums)
        if s % 3 == 0:
            return s
        
        if s % 3 == 2:
            t1, t2 = float("inf"),float("inf")
            if 2 in dic: #可以删除一个模为 2 的最小数
                t1 = dic[2][0]
                
            if len(dic[1]) >= 2: # 也可以删除两个模为 1 的最小数
                t2 = dic[1][0] + dic[1][1]
                
            if t1 > t2:# 选择两种可能中较小的值删除
                return s - t2
            
            return s - t1
        
        if s % 3 == 1:
            t1, t2 = float("inf"), float("inf")
            if 1 in dic: # 可以删除一个模为 1 的最小数
                t1 = dic[1][0]
            if len(dic[2]) >= 2: # 也可以删除两个模为 2 的最小数
                t2 = dic[2][0] + dic[2][1]
                
            if t1 > t2: # 选择两种可能中较小的值删除
                return s - t2
            
            return s - t1