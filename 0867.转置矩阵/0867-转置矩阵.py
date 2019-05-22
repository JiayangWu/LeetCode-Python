class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        
        Maxcount = len(A[0])
        count = 0
        while count < Maxcount:
            temp = []
            for sublist in A:
                temp.append(sublist[count])
            res.append(temp)
            count += 1
            
        return res
        