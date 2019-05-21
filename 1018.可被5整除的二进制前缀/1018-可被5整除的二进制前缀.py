class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        n = A[0]
        res = list()
        for i in range(0, len(A) - 1):
            if n % 5 == 0:
                res.append(True)
            else:
                res.append(False)
            n *= 2
            n += A[i + 1]
    
        if n % 5 == 0:
            res.append(True)
        else:
            res.append(False)
        return res
        