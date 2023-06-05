class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        c = Counter(s)
        return 1 == len(set(c.values()))