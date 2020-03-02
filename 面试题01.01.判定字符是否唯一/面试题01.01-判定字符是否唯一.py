class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        return len(set(astr)) == len(astr)