class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = (arr[-1] - arr[0]) // len(arr)
        
        k = arr[0]
        for num in arr:
            if num != k:
                return k
            k += d
        return k