class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        RANGE = 5 * 10 ** 4
        bucket = [0 for _ in range(2 * RANGE + 1)]

        for num in nums:
            bucket[num + RANGE] += 1

        res = []
        for index, count in enumerate(bucket):
            if count:
                res.extend([index - RANGE] * count)
        return res