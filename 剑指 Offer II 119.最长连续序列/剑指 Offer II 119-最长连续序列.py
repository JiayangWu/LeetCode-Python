class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = dict()
        res = 0
        for num in nums:
            if num not in record:
                left = record.get(num - 1, 0)
                right = record.get(num + 1, 0)
                
                length = right + left + 1
                res = max(res, length)
                for i in [num - left, num, num + right]:
                    record[i] = length
                    
        return res
