class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # pos1, pos2 = -1, 
        res = len(words)
        pos1, pos2 = -res, -res
        for idx, word in enumerate(words):
            if word == word1:
                pos1 = idx
            elif word == word2:
                pos2 = idx
            else:
                continue
            # print pos1, pos2, res, abs(pos1 - pos2)
            res = min(res, abs(pos1 - pos2))
        return res