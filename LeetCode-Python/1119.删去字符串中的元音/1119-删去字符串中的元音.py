class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = "aeiou"
        res = ""
        for char in s:
            if char not in vowels:
                res += char 
        return res