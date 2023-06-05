class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return s != t and Counter(s) == Counter(t)