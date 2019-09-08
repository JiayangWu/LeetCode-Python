class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]      
        for i in range(2, n + 1):
            fac.append(fac[-1] * i)
        digits = [i for i in range(1, n + 1)]
        
        self.res = ""
        def dfs(left_digit, tmp, kk):
            if left_digit == 0:
                self.res = tmp[:]
                return
            for digit in digits:
                kk -= fac[left_digit - 2]
                if kk <= 0:
                    kk += fac[left_digit - 2]
                    fac.pop()
                    digits.remove(digit)
                    dfs(left_digit - 1, tmp + str(digit), kk)
                    break

        dfs(n, "", k)
        return self.res