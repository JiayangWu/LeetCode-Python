class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        from collections import Counter
        
        dic_a = Counter(chars)
        
        for word in words:
            dic_w = Counter(word)
            flag = 1
            for key, val in dic_w.items():
                if key not in dic_a or dic_a[key] < val:
                    flag = 0
                    break
            if flag:
                res += len(word)
                
        return res