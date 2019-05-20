class Solution(object):
    def combinationSum2(self, c, t):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        l = len(c)
        def dfs(start, tmp):
            s = sum(tmp)
            if s == t:
                tt = sorted(tmp)
                if tt not in res:
                    res.append(tt[:])
                return
            if start >= l:
                return

            for i in range(start, l):
                
                if c[i] > t or s + c[i] > t:
                    continue
                
                tmp.append(c[i])
                dfs(i + 1, tmp)
                tmp.pop()
                    
        for i,x in enumerate(c):
            dfs(i, list())
            
        return res