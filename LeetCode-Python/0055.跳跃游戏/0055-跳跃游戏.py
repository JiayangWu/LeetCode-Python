class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur, reach = 0, nums[0]
        while 1:
            reach = max(reach, cur + nums[cur])
            if reach >= len(nums) - 1:
                return True
            if reach == cur:
                return False
            cur += 1
                