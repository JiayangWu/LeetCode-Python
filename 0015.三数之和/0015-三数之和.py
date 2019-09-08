class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i == 0 or nums[i] > nums[i - 1]:
                # num  + b + c == 0
                left = i + 1
                right = len(nums) - 1
                
                while(left < right):
                    s = num + nums[left] + nums[right]
                    if s == 0:
                        res.append([num, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while(left < right and nums[left] == nums[left - 1]):
                            left += 1
                        while(left < right and nums[right + 1] == nums[right]):
                            right -= 1
                        # break
                    elif s > 0:
                        right -= 1
                    else:
                        left += 1
                
                    
        return res
                    