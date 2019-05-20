# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            tmp = (rand7()-1)*7 + rand7()-1
            if tmp < 40:
                return tmp % 10 + 1
        