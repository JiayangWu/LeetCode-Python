class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row, col = set(), set()
        
        for r in matrix:
            row.add(min(r))

        for c in zip(*matrix):
            col.add(max(c))
        
        return list(row & col)