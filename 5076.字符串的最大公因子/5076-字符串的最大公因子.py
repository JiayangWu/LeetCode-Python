class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1,l2 = len(str1), len(str2)
        set1, set2 = set(), set()
        for i in range(l1 + 1):
            # print str1[:i]
            if self.find(str1, str1[:i]):
                set1.add(str1[:i])
                
        for i in range(l2 + 1):
            if self.find(str2, str2[:i]):
                set2.add(str2[:i])                
                
        # print set1, set2
        res = list(set1 & set2)
        res = sorted(res, key = lambda x:-len(x))
        return res[0] if res else ""
        
    def find(self, string, tmp):
        # if not tmp:
            # print tmp
        string = string.replace(tmp, "")
        # print string
        return len(string) == 0