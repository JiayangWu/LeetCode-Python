class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        step = 0
        while left < right:
            if s[left] != s[right]:
                step += 1
            left += 1
            right -= 1

        return step <= 2