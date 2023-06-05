class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 1
        res = []
        for t in target:
            while t > cur:
                res.append("Push")
                res.append("Pop")
                cur += 1
            res.append("Push")
            cur += 1
        return res