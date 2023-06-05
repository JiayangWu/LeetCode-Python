class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        dic = dict()
        for i, char in enumerate(keyboard):
            dic[char] = i
            
        res, cur_pos = 0, 0
        for char in word:
            res += abs(dic[char] - cur_pos)
            cur_pos = dic[char]           
        return res
