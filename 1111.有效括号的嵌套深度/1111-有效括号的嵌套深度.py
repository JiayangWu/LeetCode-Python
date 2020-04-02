class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        par_cnt = 0
        res = [0 for _ in seq]
        
        for i, par in enumerate(seq):
            if par == "(":
                par_cnt += 1
                res[i] = par_cnt % 2
            else:
                res[i] = par_cnt % 2
                par_cnt -= 1
        return res