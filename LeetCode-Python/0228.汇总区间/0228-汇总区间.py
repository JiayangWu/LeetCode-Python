class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        left, right = None, None
        for i, num in enumerate(nums):
            if i == 0:
                left = num
            else:
                if nums[i - 1] != num - 1:
                    right = nums[i - 1]
                    if left != right:
                        res.append(str(left) + "->" + str(right))
                    else:
                        res.append(str(left))
                    left = num

        if left != num:
            res.append(str(left) + "->" + str(num))
        else:
            res.append(str(num))
        return res

