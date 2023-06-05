class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = float("-inf")
        for s in strs:
            isNumber = True
            for char in s:
                if not char.isdigit():
                    isNumber = False
                    break
            if isNumber:
                res = max(res, int(s))
            else:
                res = max(res, len(s))
        return res