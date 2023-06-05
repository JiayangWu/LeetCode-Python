class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = dict()
        for i, char in enumerate(s):
            if char in mapping:
                if mapping[char] != t[i]: #一对多
                    return False
            else:
                if t[i] in mapping.values(): #多对一
                    return False
                mapping[char] = t[i]
        return True