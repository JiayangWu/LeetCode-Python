class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = [ch for ch in s if ch.isalpha()]
        digit = [ch for ch in s if ch.isdigit()]
        
        if abs(len(char) - len(digit)) > 1:
            return ""
        
        res = ""
        i = 0
        if len(char) > len(digit):
            while i < len(digit):
                res += char[i]
                res += digit[i]
                i += 1
            res += char[i]
            
        else:
            while i < len(char):
                res += digit[i]
                res += char[i]
                i += 1
                
            if len(char) < len(digit):
                res += digit[i]
                
        return res
                