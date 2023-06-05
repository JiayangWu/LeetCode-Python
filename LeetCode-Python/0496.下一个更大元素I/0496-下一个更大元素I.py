class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num2larger = dict()
        stack = []
        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                last_index = stack[-1]
                num2larger[nums2[last_index]] = num
                stack.pop()
            stack.append(i)

        res = []
        for num in nums1:
            if num in num2larger:
                res.append(num2larger[num])
            else:
                res.append(-1)
        return res