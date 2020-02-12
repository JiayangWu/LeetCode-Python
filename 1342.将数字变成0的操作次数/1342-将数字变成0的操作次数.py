class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num  >>= 1
            cnt += 1
        return cnt