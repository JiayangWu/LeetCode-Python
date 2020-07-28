class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        import copy
        rs = defaultdict(set)

        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                rs[i] = set(s[i])
            else:
                rs[i] = copy.deepcopy(rs[i + 1])
                rs[i].add(s[i])
                
        ls = set(s[0])
        res = 0
        for i in range(len(s) - 1):
            ls.add(s[i])
            if len(ls) == len(rs[i + 1]):
                res += 1
      
        return res