class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        res = 0
        maxx = 0
        for i in range(len(light)):
            maxx = max(light[i] - 1, maxx)
            if i == maxx:
                res += 1
        return res