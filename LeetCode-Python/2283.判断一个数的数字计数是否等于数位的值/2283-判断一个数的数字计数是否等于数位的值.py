class Solution:
    def digitCount(self, num: str) -> bool:
        from collections import Counter
        c = Counter(num)

        for index, n in enumerate(num):
            if c[str(index)] != int(n):
                # print(c[index], index, int(n))
                return False
        return True