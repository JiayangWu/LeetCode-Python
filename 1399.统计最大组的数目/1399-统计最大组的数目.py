class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        l = defaultdict(int)   

        def helper(num):
            # 计算num数位之和，eg：输入34, 返回3 + 4 = 7
            s = 0
            while num:
                num, tmp = divmod(num, 10)
                s += tmp
            return s

        for num in range(1, n + 1):
            l[helper(num)] += 1
        
        mmax = max(l.values())
        return sum([1 for item in l.values() if item == mmax])