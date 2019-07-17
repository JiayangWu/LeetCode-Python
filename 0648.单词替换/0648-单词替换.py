class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict = set(dict)
        
        s = sentence.split(" ")
        
        for i, word in enumerate(s):
            for j in range(len(word)):
                if word[:j + 1] in dict:
                    s[i] = word[:j + 1]
                    break
        return " ".join(s)