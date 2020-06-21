class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
        
        start = 0
        res = 0
        tmp = 0
        for end in range(len(s)):
            if s[end] in vowels:
                tmp += 1
            while end - start + 1 > k:
                if s[start] in vowels:
                    tmp -= 1
                start += 1
            res = max(res, tmp)
        return res