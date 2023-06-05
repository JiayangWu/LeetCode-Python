class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_multip = [1] +  [1 for _ in nums] # [1, 1, 2, 6, 24]
        postfix_multip = [1 for _ in nums] + [1] # [24,12,4, 1, 1]

        for i in range(len(nums)):
            prefix_multip[i + 1] = prefix_multip[i] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            postfix_multip[i] = nums[i + 1] * postfix_multip[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(prefix_multip[i] * postfix_multip[i])
        return res