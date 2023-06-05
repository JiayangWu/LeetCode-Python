from heapq import *
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_matrix = [[matrix[i][j] for j in range(n)] for i in range(m) ]
        min_heap = []
        for i in range(m):
            for j in range(n):
                if i or j:
                    if not i:
                        # the first row
                        xor_matrix[i][j] ^= xor_matrix[i][j - 1]
                    elif not j:
                        xor_matrix[i][j] ^= xor_matrix[i - 1][j]
                    else:
                        xor_matrix[i][j] ^= xor_matrix[i][j - 1] ^ xor_matrix[i - 1][j] ^ xor_matrix[i - 1][j - 1]
                if len(min_heap) < k:
                    heappush(min_heap, xor_matrix[i][j])
                else:
                    heappushpop(min_heap, xor_matrix[i][j])

        return min_heap[0]

         