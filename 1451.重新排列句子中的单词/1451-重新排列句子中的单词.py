class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        return " ".join(sorted(text.split(), key = lambda word: len(word))).capitalize()