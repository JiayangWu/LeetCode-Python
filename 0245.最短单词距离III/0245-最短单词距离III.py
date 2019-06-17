class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(words)
        
        if word1 != word2:
            pos1, pos2 = -1, -1
            for i, word in enumerate(words):
                if word == word1:
                    pos1 = i   
                elif word == word2:
                    pos2 = i
                if pos2 != -1 and pos1 != -1:
                    res = min(res, abs(pos1 - pos2))
        else:
            pos = -1
            for i, word in enumerate(words):
                if word == word1:
                    if pos != -1:
                        # print i, pos
                        res = min(res, i - pos)
                    pos = i
                        
        return res