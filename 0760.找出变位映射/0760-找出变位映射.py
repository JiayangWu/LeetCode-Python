class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        record = dict()
        for i, b in enumerate(B):
            record[b] = i
            
        res = [-1 for _ in range(len(A))]
        for i, a in enumerate(A):
            res[i] = record[a]
            
        return res