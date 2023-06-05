class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count, l_count = 0, 0
        res = 0
        for char in s:
            if char == "R":
                r_count += 1
            if char == "L":
                l_count += 1

            if l_count == r_count:
                l_count = 0
                r_count = 0
                res += 1
        return res