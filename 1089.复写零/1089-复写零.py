class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        i = 0
        while i < l:
            if arr[i] == 0:
                for j in range(l - 1, i + 1, -1):
                    arr[j] = arr[j - 1]
                if i + 1 < l:
                    arr[i + 1] = 0
                i += 2
            else:
                i += 1
        return arr