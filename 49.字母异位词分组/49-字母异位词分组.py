class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        dic = defaultdict(list)
        for word in strs:
            sortedword = "".join(sorted(word))
            dic[sortedword].append(word)
            
        return dic.values()