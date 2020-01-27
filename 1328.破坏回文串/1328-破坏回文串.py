class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) == 1:
            return ""
        if len(set(palindrome)) == 1:
            if palindrome[0] == "a":
                return palindrome[:-1] + "b"
        for ch in palindrome:
            if ord(ch) > ord("a"):
                res = palindrome.replace(ch, "a", 1)
                return res if res != res[::-1] else palindrome[:-1] + "b"