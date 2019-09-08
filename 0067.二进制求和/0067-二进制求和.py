class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1, l2 = len(a), len(b)
        if l1 < l2:
            l1, l2 = l2, l1
            a, b = b, a
        la, lb = [], []
        for char in a:
            la.append(int(char))
        for char in b:
            lb.append(int(char))
        la, lb = la[::-1], lb[::-1]
        
        for i in range(l1):
            if i < l2:
                la[i] += lb[i]
            if la[i] > 1:
                la[i] -= 2
                if i != l1 - 1:
                    la[i + 1] += 1
                else:
                    la.append(1)
                    
        return "".join(str(x) for x in la[::-1])
            