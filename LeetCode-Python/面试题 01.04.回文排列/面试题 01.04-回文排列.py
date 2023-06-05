class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        odd = False
        for char, freq in Counter(s).items():
            if freq % 2:
                if odd:
                    return False
                odd = True
        return True