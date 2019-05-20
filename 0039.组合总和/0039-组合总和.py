class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        
        def backtrack(remain, temp, start):
            if not remain: #remainΪ0
                res.append(temp[:])
            else:
                for i, n in enumerate(candidates[start:]):
                    if n > remain:
                        break
                    backtrack(remain-n, temp+[n], start+i)
        backtrack(target, [], 0)
        return res