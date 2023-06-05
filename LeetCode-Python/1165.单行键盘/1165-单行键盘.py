class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        char2pos = dict()

        for pos, char in enumerate(keyboard):
            char2pos[char] = pos

        res = 0
        last_pos = 0
        for char in word:  
            res += abs(last_pos - char2pos[char])
            last_pos = char2pos[char]
        return res