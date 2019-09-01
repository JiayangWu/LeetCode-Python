class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2 3 5 6 + 6
        prime_cnt = 0
        for i in range(1, n + 1):
            if self.prime(i):
                prime_cnt += 1
        non_prime_cnt = n - prime_cnt
        # print prime_cnt, non_prime_cnt
        return (math.factorial(prime_cnt) * math.factorial(non_prime_cnt)) % (10 ** 9 + 7)
        
    def prime(self, n):
        if n == 1:
            return False
        if n == 2 or n == 3 or n == 5:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
        