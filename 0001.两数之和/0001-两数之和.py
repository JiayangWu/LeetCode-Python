class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, x in enumerate(nums):
            if hashmap.has_key(target - x):
                return [hashmap[target - x], i]
            else:
                hashmap[x] = i
                
        return []