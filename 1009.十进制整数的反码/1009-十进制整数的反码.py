class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        # print b
        
        res = ""
        for char in b:
            if char == "0":
                res += "1"
            else:
                res += "0"
                
        return int(res, 2)