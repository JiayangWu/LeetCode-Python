class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # print int(n**0.5 +1)
        if n <= 2:
            return 0
        temp =[1 for i in range(1,n+1)]
        temp[0], temp[1]  = 0,0
        for i in range(2, int(n**0.5 +1)):
            if temp[i] == 1:
                for j in range(i*i, n, i):
                    temp[j] = 0
            # print temp
        return sum(temp)
            
        