class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l = 0
        for num in arr:
            if num % 2:
                l += 1
                if l == 3:
                    return True 
            else:
                l = 0
        return False