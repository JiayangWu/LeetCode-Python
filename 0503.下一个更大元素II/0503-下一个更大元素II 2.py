class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        max_element = max(nums)
        stack = list()
        res = [-1 for i in range(len(nums))]
        
        for i, x in enumerate(nums):
                
            if not stack or nums[stack[-1]] >= x:
                stack.append(i)
            else:
                # print stack, res
                while(stack and nums[stack[-1]] < x):
                      res[stack[-1]] = x
                      stack.pop()
                if x != max_element:#最大的不用放进栈，直接默认-1就好
                    stack.append(i)
                    
        # print stack, res            
        if stack: #还有需要循环搜索的元素
            for i, x in enumerate(nums):
                if not stack:
                      break
                while stack and x > nums[stack[-1]]:
                      res[stack[-1]] = x
                      stack.pop()
                     
        return res