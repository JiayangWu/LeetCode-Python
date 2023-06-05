class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def happy(num):
            res = 0
            while num:
                num, tmp = divmod(num, 10)
                res += tmp ** 2
            return res
        visited = set()
        while n and n not in visited:
            visited.add(n)
            tmp = happy(n)
            if tmp == 1:
                return True
            n = tmp
        return False