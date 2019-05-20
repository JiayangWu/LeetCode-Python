class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        l = [a, b, c]
        l.sort()
        minmove, maxmove = 0, 0
        if l[0] + 1 != l[1]:
            minmove += 1
            maxmove += l[1] - l[0] - 1
        if l[1] + 1 != l[2]:
            minmove += 1
            maxmove += l[2] - l[1] - 1
        if l[1] - l[0] == 2 or l[2] - l[1] == 2:
            minmove = 1
        return [minmove, maxmove]