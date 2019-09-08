class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = digits[::-1]
        
        l[0] += 1
        for i in range(len(l)):
            if l[i] > 9:
                l[i] -= 10
                if i != len(l) - 1:
                    l[i + 1] += 1
                else:
                    l.append(1)
        return l[::-1]