class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        
        if  (Y % 100 != 0 and Y % 4 ==0) or (Y % 100 == 0 and Y % 400 == 0) :
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][M - 1]
        else:
            return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][M - 1]
        