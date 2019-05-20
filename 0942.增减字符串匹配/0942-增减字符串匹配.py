class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        res = []
        for char in S:
            if char == "I":
                res.append(left)
                left  += 1
            else:
                res.append(right)
                right -= 1
        res.append(right)
        return res
        
        