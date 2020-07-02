class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return (x3 - x2) * (x4 - x1) < 0 and (y3 - y2) * (y4 - y1) < 0