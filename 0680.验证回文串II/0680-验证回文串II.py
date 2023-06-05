class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = False
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                if not delete:
                    delete = True
                    break
            left += 1
            right -= 1
            
        if delete:
            s1 = s[:left] + s[left + 1:]
            s2 = s[:right] + s[right + 1:]
            return s1 == s1[::-1] or s2 == s2[::-1]
        else:
            return True
        