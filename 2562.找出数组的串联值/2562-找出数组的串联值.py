class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        while nums:
            if len(nums) > 1:
                serial = int(str(nums[0]) + str(nums[-1]))
            else:
                serial = nums[0]
            res += serial
            nums = nums[1:-1]
        return res