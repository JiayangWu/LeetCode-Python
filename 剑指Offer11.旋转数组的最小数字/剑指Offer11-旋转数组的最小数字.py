class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        return min(numbers)
        # if not numbers:
        #     return None

        # if numbers[0] < numbers[-1]:
        #     return numbers[0]

        # left, right = 0, len(numbers)

        # while left <= right:
        #     mid = (left + right) // 2

        #     if numbers[mid] < numbers[mid - 1]:
        #         return numbers[mid]
        #     elif numbers[mid] 