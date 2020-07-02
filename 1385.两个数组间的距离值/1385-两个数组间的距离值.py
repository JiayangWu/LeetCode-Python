class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0

        for num1 in arr1:
            flag = 1
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = 0
                    break
            if flag:
                res += 1

        return res