class Solution:
    def countLetters(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        while right < len(s):
            while right < len(s) and s[left] == s[right]:
                right += 1
            consecutive_chars_count = right - left
            res += consecutive_chars_count * (consecutive_chars_count + 1) // 2
            left = right
        return res


