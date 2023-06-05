class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        dic = {}
        for i, char in enumerate(pattern):
            if char not in dic:
                dic[char] = s[i]
            else:
                if dic[char] != s[i]:
                    return False

        return len(set(dic.values())) == len(dic.values())
                