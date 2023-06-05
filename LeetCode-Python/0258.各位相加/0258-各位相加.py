class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            new_nums = 0
            while num:
                num, n = divmod(num, 10)
                new_nums += n
            num = new_nums
        return num