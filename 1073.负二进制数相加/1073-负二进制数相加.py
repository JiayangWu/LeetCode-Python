class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = self.convertToDec(arr1) + self.convertToDec(arr2)
        l = []
        if res == 0:
            return [0]
        while res:
            d, m = divmod(res, -2)
            res = - (res // 2)
            l.append(-m)
        return l[::-1]

    def convertToDec(self, arr):
        res = 0
        for index, digit in enumerate(arr[::-1]):
            res += digit * ((-2) ** index)
        return res


        