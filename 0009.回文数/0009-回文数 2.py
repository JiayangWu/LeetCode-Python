class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #2019.6.1
        xx = x
        if x < 0:
            return False

        reverse = 0
        while x > 0:
            x, tmp = divmod(x, 10)
            reverse = reverse * 10 + tmp

        return reverse == xx