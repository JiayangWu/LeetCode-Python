class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while 1:
            if n == 1:
                return True
            visited.add(n)
            n = sum([int(digit) ** 2 for digit in str(n)])
            if n in visited:
                return False
