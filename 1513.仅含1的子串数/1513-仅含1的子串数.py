class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        cons_length = 0
        res = 0
        MOD = 10 ** 9 + 7
        for ch in s:
            if ch == '1':
                cons_length += 1
            else:
                res = (res + (1 + cons_length) * cons_length // 2) % MOD
                cons_length = 0
        return (res + (1 + cons_length) * cons_length // 2) % MOD