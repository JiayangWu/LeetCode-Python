class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        mask = 1
        for i in range(32):
            cnt_one = 0
            for num in nums:
                cnt_one += 1 if num & mask else 0 
                
            res += cnt_one * (len(nums) - cnt_one)
            mask = mask << 1
        return res
        
                