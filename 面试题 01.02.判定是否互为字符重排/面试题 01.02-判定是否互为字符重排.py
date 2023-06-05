class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        from collections import Counter
        return Counter(s1) == Counter(s2)