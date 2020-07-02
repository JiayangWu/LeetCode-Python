class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        MOD = 10 ** 9 + 7 
        cnt = 1
        pre, cur = 0, 1
        while cnt < n:
            tmp = cur + pre
            pre = cur 
            cur = tmp
            cnt += 1
        return cur % MOD