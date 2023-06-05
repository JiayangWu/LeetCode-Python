class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n)[2:].count("1") == 1 if n > 0 else False