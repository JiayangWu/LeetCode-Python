class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = right_max
            right_max = max(right_max, tmp)
        return arr