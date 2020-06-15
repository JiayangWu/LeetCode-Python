class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        maxValues, minValues = float("-inf"), float("inf")
        s = str(num)
        for x in range(0, 10):
            for y in range(0, 10):
                val = s.replace(str(x), str(y))
                if val[0] != '0' and int(val) != 0:
                    maxValues = max(maxValues, int(val))
                    minValues = min(minValues, int(val))
                    
        return maxValues - minValues