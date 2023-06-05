class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        c = Counter(nums)
        res = []
        for num, freq in c.items():
            while len(res) < freq:
                res.append([])

            for i in range(freq):
                res[i].append(num)
        return res
