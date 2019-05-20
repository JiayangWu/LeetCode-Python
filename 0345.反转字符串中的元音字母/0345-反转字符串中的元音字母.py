class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        s = [char for char in s]
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = l - 1
        while(left < right):
            while(left <= l -1 and s[left] not in vowel):
                left += 1
            while(right >= 0 and s[right] not in vowel):
                right -= 1
            if left < right and s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)