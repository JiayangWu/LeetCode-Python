class Solution:
    def minNumBooths(self, demands: List[str]) -> int:
        from collections import defaultdict, Counter
        char2count = defaultdict(int)
        for demand in demands:
            c = Counter(demand)

            for char, freq in c.items():
                char2count[char] = max(char2count[char], freq)

        return sum(freq for freq in char2count.values())