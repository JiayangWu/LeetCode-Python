class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = sorted(arr)
        dic, rank = {}, 0
        pre_num = None
        for i, num in enumerate(l):
            if pre_num != num:
                rank += 1
                dic[num] = rank
                pre_num = num
        
        res = []
        for num in arr:
            res.append(dic[num])
        return res