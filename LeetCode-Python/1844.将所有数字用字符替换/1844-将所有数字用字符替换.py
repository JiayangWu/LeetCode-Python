class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(0, len(s), 2):
            char = s[i]

            if i + 1 < len(s):
                shift = int(s[i + 1])
                res += char + chr(ord(char) + shift)
            else:
                res += char
        return res