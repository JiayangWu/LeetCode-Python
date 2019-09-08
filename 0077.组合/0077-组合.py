class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(t, cnt, tmp):
            if cnt == 0:
                res.append(tmp[:])

            for i in range(t + 1, n + 1):
                dfs(i, cnt - 1, tmp + [i])
            
        dfs(0, k, [])
        return res
            