class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        def convertInt(string):
            tmp = 1
            string = string[::-1]
            res = 0
            for i, x in enumerate(string):
                res += tmp * int(x)
                tmp *= -2
                
            return res
        n1 = convertInt(arr1)
        n2 = convertInt(arr2)
        # print n1, n2, convertInt(self.baseNeg2(n1 + n2))
        return self.baseNeg2(n1 + n2)
    
    
    
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = []
        # n = N
        while N:
            N, b = divmod(N, 2)
            N = -N
            res.append(str(b))
        return "".join(res[::-1]) or "0"
        # return "0" if not n else "".join(res[::-1])
