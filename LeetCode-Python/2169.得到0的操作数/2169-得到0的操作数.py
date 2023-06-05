class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0
        while num1 and num2:
            res += 1
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1

        return res