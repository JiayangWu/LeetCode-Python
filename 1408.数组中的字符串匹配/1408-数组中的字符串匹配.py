class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        fix = set() 
        res = []
        
        for word1 in words:
            for word2 in words:
                if len(word1) < len(word2) and word1 in word2:
                        res.append(word1)
                        break 

        return res