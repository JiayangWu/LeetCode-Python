class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            tmp = 0
            for num in nums:
                tmp += math.ceil(num * 1.0 / mid)
                if tmp > threshold:
                    break 
            
            if tmp > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
