class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        s = set(s)
        for char in s:
            if char.lower() in s and char.upper() in s:
                if not res or char.upper() > res:
                    res = char.upper()
        return res