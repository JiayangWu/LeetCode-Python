class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return matrix
        
        from heapq import *
        queue = []
        for i in range(len(matrix)):
            heappush(queue, (matrix[i][0], i, 0))
        
        cnt = 0
        while cnt < k:
            cnt += 1
            
            val, row, col = heappop(queue)
            if col + 1 < len(matrix):
                heappush(queue, (matrix[row][col + 1], row, col + 1))
            
        return val
            