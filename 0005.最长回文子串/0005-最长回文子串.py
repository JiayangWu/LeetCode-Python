class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, 0
        res, string = 0, ""
        for i in range(len(s)):
            left, right = i, i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            
            if right - left + 1 > res:
                res = right - left + 1
                string = s[left:right + 1]
                
        for i in range(1, len(s)):
            left, right = i - 1, i
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            
            if right - left + 1 > res:
                res = right - left + 1
                string = s[left:right + 1]      
        return string
        