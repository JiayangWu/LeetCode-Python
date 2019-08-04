class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        # print text
        for i in range(1, len(text)):
            if text[:i] == text[len(text) - i:]:
                return 2 + self.longestDecomposition(text[i:len(text) - i])
        return 1 if text else 0