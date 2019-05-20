class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def generate(k, i, tmp):
            
            if k == 0:
                res.append(tmp[:])
                return
            
            for j in range(i , n + 1):
                tmp.append(j)
                generate(k - 1, j + 1, tmp)
                tmp.pop()
            
        
        generate(k, 1, [])
        return res
        