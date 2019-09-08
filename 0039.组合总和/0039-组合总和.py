class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(t, tmp):
            if t < 0:
                return
            if t == 0:
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            
            for i, x in enumerate(candidates):
                if t - x < 0:
                    break
                dfs(t - x, tmp + [x])
        
        
        dfs(target, [])
        return res