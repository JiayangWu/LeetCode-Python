class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalpha() or char.isdigit()])
        print(s)
        return s == s[::-1]