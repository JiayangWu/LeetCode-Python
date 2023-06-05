from heapq import *
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        min_sum = sum([mat[i][0] for i in range(m)])
        min_heap = [(min_sum, [0 for i in range(m)])]
        cur = 0
        visited = set()
        while cur < k:
            s, indices = heappop(min_heap)
            cur += 1
            if cur == k:
                return s

            for i in range(m):
                if indices[i] + 1 < n:
                    nxt_s = s - mat[i][indices[i]] + mat[i][indices[i] + 1]
                    nxt_indices = indices[:]
                    nxt_indices[i] += 1
                    str_indices = "".join([str(i) for i in nxt_indices])
                    if str_indices not in visited:
                        visited.add(str_indices)
                        heappush(min_heap, (nxt_s, nxt_indices))
        