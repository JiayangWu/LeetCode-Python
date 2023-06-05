class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B == 1:
            return A
        if B == 0:
            return 0
        return A + self.multiply(A, B - 1)