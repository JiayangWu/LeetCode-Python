class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char2word = dict()
        word2char = dict()
        
        for i in range(len(s)):
            char, word = s[i], t[i]
            if char not in char2word:
                char2word[char] = word 
            else:
                if char2word[char] != word:
                    return False

            if word not in word2char:
                word2char[word] = char
            else:
                if word2char[word] != char:
                    return False
            
        return True