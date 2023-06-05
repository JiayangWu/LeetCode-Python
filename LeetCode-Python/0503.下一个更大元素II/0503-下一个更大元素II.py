class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1 for _ in nums]
        for i, num in enumerate(nums + nums):
            while stack and nums[stack[-1]] < num:
                last_index = stack[-1]
                res[last_index] = num
                stack.pop()
            if i < len(nums):
                stack.append(i)

        return res