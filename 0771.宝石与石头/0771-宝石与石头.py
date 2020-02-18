class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        res = 0
        for s in S:
            if s in J:
                res += 1
        return res 