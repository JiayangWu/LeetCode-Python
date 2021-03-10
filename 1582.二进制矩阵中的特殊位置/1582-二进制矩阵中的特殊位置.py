class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # 找出所有满足条件的行和列
        possible_rows = [i for i, row in enumerate(mat) if sum(row) == 1]
        possible_cols = [i for i, col in enumerate(zip(*mat)) if sum(col) == 1]
        
        # 在满足条件的行和列里统计值为1的点
        return sum([mat[i][j] for i in possible_rows for j in possible_cols])