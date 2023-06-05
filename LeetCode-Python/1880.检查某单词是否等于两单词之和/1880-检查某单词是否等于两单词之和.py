class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.sumOfDigit(firstWord) + self.sumOfDigit(secondWord) == self.sumOfDigit(targetWord)

    def sumOfDigit(self, word):
        res = ""
        for char in word:
            res += str(ord(char) - ord("a"))
        return int(res)