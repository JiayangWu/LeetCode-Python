class Solution:
    def minimumCost(self, s: str) -> int:
        # 110101
        # 111010 min(i, n - i)
        prev = s[0]
        res = 0
        for i, char in enumerate(s):
            if i and char != prev:
                # flip is required:
                res += min(i, len(s) - i)
                prev = char
        return res