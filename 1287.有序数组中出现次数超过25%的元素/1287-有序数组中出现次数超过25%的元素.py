class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = 1
        for i, num in enumerate(arr):
            if i:
                if num == arr[i - 1]:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > len(arr) / 4:
                return num
            