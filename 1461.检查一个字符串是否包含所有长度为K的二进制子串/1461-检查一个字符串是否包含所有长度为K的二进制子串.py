class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        numSet = set()
        for i in range(len(s) - k + 1):
            numSet.add(int(s[i:i + k], 2))
        
        for num in range(2 ** k):
            if num not in numSet:
                return False
        return True