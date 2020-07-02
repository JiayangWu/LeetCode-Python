class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        b = [[0 for _ in range(len(colsum))] for _ in range(2)]

        for i, cs in enumerate(colsum):
            if cs == 2:
                b[0][i] = 1
                b[1][i] = 1
                upper -= 1
                lower -= 1
        for i, cs in enumerate(colsum):
            if cs == 1:
                if lower > upper:
                    b[1][i] = 1
                    lower -= 1
                else:
                    b[0][i] = 1
                    upper -= 1
        if upper != 0 or lower != 0:
            return []
        return b