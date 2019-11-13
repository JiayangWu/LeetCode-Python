class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s = s1 + s2
        x = s.count("x")
        if len(s1) != len(s2) or x % 2 == 1 or (len(s) - x) % 2 == 1:
            return -1

        pair1 = 0
        pair2 = 0
        for i in range(len(s1)):
            if s1[i] == "y" and s2[i] == "x":
                pair1 += 1
            elif s1[i] == "x" and s2[i] == "y":
                pair2 += 1
    
        return pair1 // 2 + pair2 // 2 + pair1 % 2 + pair2 % 2