class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        
        arr = set(arr) - set([0])

        for x in arr:
            if x * 2 in arr:
                return True
            
        return False
        
        