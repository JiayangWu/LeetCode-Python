class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        res_left = ""
        res_right = ""
        while left < right:
            res_left += min(s[left], s[right])
            res_right = min(s[left], s[right]) + res_right
            left += 1
            right -= 1
        
        if left == right:
            res = res_left + s[left] + res_right
        else:
            res = res_left + res_right
        return res