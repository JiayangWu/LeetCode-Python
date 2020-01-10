class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {0:1, 1:1}

        for i in range(2, n + 1):
            cnt = 0
            for l in range(0, i):
                cnt += dic[l] * dic[i - 1 - l]
            dic[i] = cnt 

        return dic[n]