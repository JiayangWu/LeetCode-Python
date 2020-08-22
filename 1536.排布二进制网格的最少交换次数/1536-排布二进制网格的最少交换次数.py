class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque
        dic = dict()
        n = len(grid)
        for i, row in enumerate(grid):
            cnt = 0
            for j in range(n - 1, -1, -1):
                if not row[j]:
                    cnt += 1
                else:
                    break
            dic[i] = cnt

        res = 0
        for i in range(n):
            zero_cnt = dic[i]

            if zero_cnt < n - i - 1:
                for j in range(i + 1, n):
                    if dic[j] >= n - i - 1:
                        break 
                if dic[j] < n - i - 1:
                    return -1
                tmp = dic[j]
                res += j - i
                for k in range(j, i, -1):
                    dic[k] = dic[k - 1]
            
        return res
