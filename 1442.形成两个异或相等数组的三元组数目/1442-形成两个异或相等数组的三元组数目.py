class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(arr)):
            preSum = arr[i]
            for j in range(i + 1, len(arr)):
                preSum ^= arr[j]
                if not preSum:
                    res += j - i

        return res