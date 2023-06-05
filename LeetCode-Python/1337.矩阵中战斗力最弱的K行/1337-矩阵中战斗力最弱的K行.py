class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pair = [(i, sum(row)) for i, row in enumerate(mat)]
        pair.sort(key = lambda x: x[1])
        return [p[0] for p in pair[:k]]