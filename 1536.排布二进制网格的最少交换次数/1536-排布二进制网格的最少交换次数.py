class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dic = dict() # key 是每行的idx， val 是这一行末尾0的个数
        n = len(grid)
        for i, row in enumerate(grid): # 统计每一行末尾有几个0
            cnt = 0
            for j in range(n - 1, -1, -1):
                if not row[j]:
                    cnt += 1
                else:
                    break
            dic[i] = cnt

        res = 0
        for i in range(n):
            if dic[i] < n - i - 1: # 这一行0太少，需要放到下面去
                for j in range(i + 1, n):
                    if dic[j] >= n - i - 1: # 找到0足够多的行
                        break 
                if dic[j] < n - i - 1: # 没找到说明无解
                    return -1

                for k in range(j, i, -1): #把第i行换到第j行的位置上去
                    dic[k] = dic[k - 1]

                res += j - i
        return res