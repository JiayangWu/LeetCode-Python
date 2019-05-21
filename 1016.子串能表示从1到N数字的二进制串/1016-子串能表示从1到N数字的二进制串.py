class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for i in range(1, N + 1):
            # print str(bin(i)[2:])
            if str(bin(i)[2:]) not in S:
                return False
        
        return True