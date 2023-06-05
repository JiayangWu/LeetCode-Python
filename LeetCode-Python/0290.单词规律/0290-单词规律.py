class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char2word = dict()
        word2char = dict()

        words = [word for word in s.split()]
        if len(words) != len(pattern):
            return False
        
        for i in range(len(words)):
            char, word = words[i], pattern[i]
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