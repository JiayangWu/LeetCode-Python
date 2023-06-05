class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1, s2 = s[:len(s) // 2], s[len(s) // 2:]
        return self.countVowels(s1) == self.countVowels(s2)

    def countVowels(self, s):
        vowels = "aeiouAEIOU"
        return sum(char in vowels for char in s)