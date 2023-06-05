class Solution:
    def similarPairs(self, words: List[str]) -> int:
        from collections import defaultdict
        pattern2count = defaultdict(int)
        for word in words:
            pattern2count["".join(sorted(list(set(word))))] += 1

        res = 0
        for pattern, count in pattern2count.items():
            res += count * (count - 1) // 2
        return res