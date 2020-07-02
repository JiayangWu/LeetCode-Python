from math import factorial as fac
class Solution(object):
    def numberOfWays(self, num_people):
        """
        :type num_people: int
        :rtype: int
        """
        def catalan(n):
            return fac(2*n) // (fac(n+1) * fac(n))
        return catalan(num_people // 2) % ( 10 ** 9 + 7)