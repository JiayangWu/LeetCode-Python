class Solution(object):
    def numJewelsInStones(self, J, S):
        if len(J) == 0 or len(S) == 0:
            return 0
        count = 0
        for itemins in S:
            if itemins in J:
                count += 1
                
        return count
        