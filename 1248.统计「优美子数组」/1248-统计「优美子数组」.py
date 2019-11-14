class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        odd = []
        for i, num in enumerate(nums):
            if num % 2:
                odd.append(i)
                
        if len(odd) < k:
            return 0
        
        
        for i in range(len(odd)):
            if i + k > len(odd):
                break
            if i:
                last = odd[i - 1]
            else:
                last = -1
           
            if i + k < len(odd):
                nxt = odd[i + k]
            else:
                nxt = len(nums) 
                
            left = odd[i] - last    
            right = nxt - odd[i + k - 1]
            res += left * right
        return res