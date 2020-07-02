class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        first, second = 1, 1
        fib = [1, 1]
        while second < k:
            nxt = first + second 
            fib.append(nxt)
            first = second 
            second = nxt
        res = 0
        while k > 0:
            idx = bisect.bisect_left(fib, k)
            if fib[idx] == k:
                k -= fib[idx]
            else:
                k -= fib[idx - 1]
            res += 1
        return res