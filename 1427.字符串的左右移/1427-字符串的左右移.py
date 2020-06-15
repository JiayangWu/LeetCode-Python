class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        for d, amount in shift:
            if d == 0:
                s = s[amount:] + s[:amount]
            else:
                s = s[-amount:] + s[:-amount] 

        return s