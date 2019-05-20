class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return None

        aa = a.split("+")
        ra = aa[0]
        va = aa[1][:-1]
        
        bb = b.split("+")
        rb = bb[0]
        vb = bb[1][:-1]
        
        # print ra, va, rb, vb
        
        rres = int(ra) * int(rb) - int(va) * int(vb)
        vres = int(ra) * int(vb) + int(rb) * int(va)
        
        return "{}+{}i".format(str(rres), str(vres))