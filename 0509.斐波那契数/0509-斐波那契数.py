class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        F = [0,1,1]
        for i in range(3, N+1):
            F.append(F[-1] + F[-2])
        return F[N]
        