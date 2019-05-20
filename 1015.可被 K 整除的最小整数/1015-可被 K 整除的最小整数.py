class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0:
            return -1
        if K == 1:
            return 1
        n = 1
        cnt = 1
        while(n % K != 0):
            n = (n * 10 + 1) % K
            cnt += 1
            if cnt == 100000:
                break
        if cnt == 100000:
            return -1
        return cnt
            