class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mode, count = None, 0
        for num in nums:
            if not mode:
                mode = num
                count = 1
            else:
                if num != mode:
                    count -= 1
                    if count == 0:
                        mode = num
                        count = 1
                else:
                    count += 1
        return mode