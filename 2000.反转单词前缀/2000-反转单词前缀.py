class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.count(ch):
            index = word.index(ch)
            return word[:index + 1][::-1] + word[index + 1:]
        else:
            return word