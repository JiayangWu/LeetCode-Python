class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        record = [1] * n
        for i in range(2, n):
            if record[i] == 1:
                for j in range(i * 2, n, i):
                    record[j] = 0
        return sum(record) - 2 if n > 1 else 0