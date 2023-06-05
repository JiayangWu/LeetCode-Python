class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            i2 = i * i
            self.possible(i)
            if self.res:
                res += i2
        return res
            
    def possible(self, num):
        # 判断 1296 是否可以分成 1 + 29 + 6 == 36
        self.res = False
        def helper(n, s):
            # 首次递归 n = 36, s = 1296
            if not s or n > int(s):
                return
            if int(s) == n:
                self.res = True
                return
            for i in range(1, len(str(n)) + 1):
                # 下次递归 n = 30, s = 129
                helper(n - int(s[-i:]), s[:-i])
        helper(num, str(num * num))

        
        