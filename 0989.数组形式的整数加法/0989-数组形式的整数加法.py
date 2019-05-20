class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        stra = ""
        for digit in A:
            stra += str(digit)
            
        s = str(int(stra) + K)
        
        return [int(x) for i, x in enumerate(s)]
            
        