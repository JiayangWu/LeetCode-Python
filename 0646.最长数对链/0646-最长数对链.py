class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key = lambda x: x[1])
        
        end = pairs[0][0] - 1
        res = 0
        for pair in pairs:
            if pair[0] > end:
                res += 1
                end = pair[1]
        
        return res