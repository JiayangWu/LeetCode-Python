class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0 for _ in range(length + 1)]
        
        for update in updates:
            start, end, inc = update[0], update[1], update[2]
            res[start] += inc
            res[end + 1] -= inc
        
        for i in range(1, length):
            res[i] += res[i - 1]
            
        return res[:-1]