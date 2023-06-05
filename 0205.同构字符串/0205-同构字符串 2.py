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
                if mapping[char] != t[i]: #һ�Զ�
                    return False
            else:
                if t[i] in mapping.values(): #���һ
                    return False
                mapping[char] = t[i]
        return True