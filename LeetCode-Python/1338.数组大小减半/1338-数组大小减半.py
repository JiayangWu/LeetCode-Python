class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        c = Counter(arr)
        l = []
        visited = set()
        for val in arr:
            if val not in visited:
                l.append((c[val], val))
                visited.add(val)
        l.sort(key = lambda x:-x[0])

        res, reduced_size = 0, 0
        for freq, val in l:
            reduced_size += freq
            res += 1
            if reduced_size >= len(arr) // 2:
                return res