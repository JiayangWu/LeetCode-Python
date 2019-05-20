class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
      
        res = 0
        for col in zip(*A):
            if sorted(col) != list(col):
                res += 1
          
                
        return res
                    