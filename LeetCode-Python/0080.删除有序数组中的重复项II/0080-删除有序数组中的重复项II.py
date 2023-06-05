class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, prev_count = nums[0], 1
        res = 1
        for num in nums[1:]:
            if num == prev:
                if prev_count == 1:
                    nums[res] = num
                    res += 1
                prev_count += 1
            else:
                nums[res] = num
                res += 1
                prev = num
                prev_count = 1
        return res
            