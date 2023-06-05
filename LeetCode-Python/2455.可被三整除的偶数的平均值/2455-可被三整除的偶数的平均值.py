class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, cnt = 0, 0
        for num in nums:
            if num % 6 == 0:
                cnt += 1
                s += num
        return int(s / cnt) if cnt else 0