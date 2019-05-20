class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l = len(A)

        val = []
        for j in range(1,7):
            flag = 0
            for i, item in enumerate(A):       
                if A[i] != j and B[i] != j:
                    flag = 1
                    break
                if flag == 1:
                    break
            if flag == 0:
                val.append(j)
                
        # print val
        if not val:
            return -1
        
        mintimes = []     
        for item in val:
            mintimes.append(min(l - A.count(item), l - B.count(item) ))
            
        return min(mintimes)
        
        