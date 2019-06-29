class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        if len(S) < K:
            return 0
        res = 0
        for i in range(len(S) - K + 1):
            # for j in range(i + K, len(S)):
            tmp = S[i:i + K]
            if self.check(tmp):
                res += 1
        return res
            
        
    def check(self, string):
        # record = {}
        from collections import Counter
        record = Counter(string)
        # print record
        for key, val in record.items():
            if val > 1:
                return False
        # print string
        return True