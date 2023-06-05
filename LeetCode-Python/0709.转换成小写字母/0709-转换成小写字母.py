class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for char in s:
            res += char.lower()
        return res