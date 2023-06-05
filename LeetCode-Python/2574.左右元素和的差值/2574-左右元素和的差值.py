class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]

        for num in nums[:-1]:
            left_sum.append(num + left_sum[-1])

        for num in nums[::-1][:-1]:
            right_sum.append(num + right_sum[-1])

        return [abs(l - r) for l, r in zip(left_sum, right_sum[::-1])]