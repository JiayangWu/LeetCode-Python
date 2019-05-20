class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y
        if Y % 2 == 0:
            return 1 + self.brokenCalc(X, Y // 2)
        else:
            return 1 + self.brokenCalc(X, (Y + 1))
        