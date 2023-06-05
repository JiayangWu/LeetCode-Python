class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        for index, char1 in enumerate(word1):
            res += char1
            if index < len(word2):
                res += word2[index]
        
        if index < len(word2):
            res += word2[index + 1:]
        return res