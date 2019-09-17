class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        if tx < sx or ty < sy:
            return False
        if tx == sx and (ty - sy) % sx == 0:
            return True
        if ty == sy and (tx - sx) % sy == 0:
            return True
        return self.reachingPoints(sx, sy, tx % ty, ty % tx)