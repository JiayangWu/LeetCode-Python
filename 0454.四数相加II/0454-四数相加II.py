class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map1 = defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                t = a + b
                map1[t] += 1
                
        for c in C:
            for d in D:
                t = - c - d
                res += map1[t]
                    
        return res
                

                