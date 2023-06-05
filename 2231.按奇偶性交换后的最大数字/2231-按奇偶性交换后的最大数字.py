class Solution:
    def largestInteger(self, num: int) -> int:
        odd = sorted([int(digit) for digit in str(num) if digit in "13579"])
        even = sorted([int(digit) for digit in str(num) if digit not in "13579"])
        res = 0
        for digit in str(num):
            if int(digit) % 2:
                res = res * 10 + odd.pop()
            else:
                res = res * 10 + even.pop()
        
        return res
