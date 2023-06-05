class Solution:
    def findWords(self, words: List[str]) -> List[str]: 
        row_1 = "qwertyuiop"
        row_2 = "asdfghjkl"
        row_3 = "zxcvbnm"
        res = []
        for word in words:
            l_word = word.lower()
            row = ""
            if l_word[0] in row_1:
                row = row_1
            elif l_word[0] in row_2:
                row = row_2   
            elif l_word[0] in row_3:
                row = row_3

            inSameRow = True
            for char in l_word:
                if char not in row:
                    inSameRow = False
                    break 
            
            if inSameRow:
                res.append(word)
        return res