class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(start, t, tmp):
            if t == 0:
                tmp.sort()
                if tmp not in res:
                    res.append(tmp)
                return
            
            for i in range(start, len(candidates)):
                x = candidates[i]
                if t - x < 0:
                    break
                dfs(i + 1, t - x, tmp + [x])
        
        
        dfs(0, target, [])
        return res