class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                if item not in result:
                    result.append(item[:])
        return result
    
