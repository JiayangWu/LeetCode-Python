class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(int)
        res = 0
        for i, x in enumerate(dominoes):
            pair = (x[1], x[0])
            if x[0] < x[1]:
                pair = (x[0], x[1])
            res += dic[pair]
            dic[pair] += 1
            
        return res