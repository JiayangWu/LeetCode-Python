class Solution:
    def getLucky(self, s: str, k: int) -> int:

        num = ""
        for char in s:
            num += str(ord(char) - ord("a") + 1)

        num = int(num)
        while k:
            new_num = 0
            while num:
                num, m = divmod(num, 10)
                new_num += m
            num = new_num
            k -= 1
        return num
