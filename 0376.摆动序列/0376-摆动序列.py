class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        autom = {}
        max_l = 1
        state = "begin"
        for i in range(1, len(nums)):
            if state == "begin":
                if nums[i-1] < nums[i]:
                    state = "up"
                    max_l += 1
                elif nums[i-1] > nums[i]:
                    state = "down"
                    max_l += 1
                    
            elif state == "up":
                if nums[i-1] > nums[i]:
                    state = "down"
                    max_l += 1
                    
            elif state == "down":
                if nums[i-1] < nums[i]:
                    state = "up"
                    max_l += 1
                    
        return max_l
                