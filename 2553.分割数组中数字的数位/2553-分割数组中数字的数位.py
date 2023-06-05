class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            for digit in str(num):
                res.append(int(digit))
        return res