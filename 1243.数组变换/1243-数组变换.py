class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flag = 1
        while flag:
            flag = 0
            res = [num for num in arr]
            for i in range(1, len(arr) - 1):
                if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    res[i] -= 1
                    flag = 1
                elif arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
                    res[i] += 1
                    flag = 1
            arr = res[:]
        return res
            