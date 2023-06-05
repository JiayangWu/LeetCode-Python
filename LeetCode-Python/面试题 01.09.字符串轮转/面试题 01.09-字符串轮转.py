class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if not s2:
            return not s1
        return s2 in s1 + s1