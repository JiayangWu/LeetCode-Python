class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        from collections import defaultdict

        record = defaultdict(int)

        res = 0
        for i in range(len(s) - minSize + 1):
            substring = s[i:i+minSize]
            if len(set(substring)) <= maxLetters:
                record[substring] += 1
                res = max(res, record[substring])

        return res 