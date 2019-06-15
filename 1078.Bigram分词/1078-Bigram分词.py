class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        text = text.split(" ")
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                res.append(text[i + 2])
                
        return res