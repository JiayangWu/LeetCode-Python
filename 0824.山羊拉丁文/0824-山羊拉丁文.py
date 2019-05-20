class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        res = []
        T = S.split(" ")
        for index, word in enumerate(T):
            temp = word
            if word[0] in vowel:
                temp += "ma"
            else:
                temp = temp[1:] + temp[0] + "ma"
                
            temp += "a" * (index + 1)           
            res.append(temp)
        
        return " ".join(item for item in res)