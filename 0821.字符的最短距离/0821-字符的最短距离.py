class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        record = []
        
        for i, char in enumerate(S):
            if char == C:
                record.append(i)
        # print record
        res = []
    
        for i, char in enumerate(S):
            if char != C:
                res.append(self.findClosestC(i, record))
            else:
                res.append(0)
                
        return res
    
    def findClosestC(self, i, record):
        left = 0
        right = len(record) - 1
        
        while(left < right and left + 1 != right):
            mid = left + (right - left) / 2
            # print i,mid
            if record[mid] > i:
                right = mid
            if record[mid] < i:
                left = mid
        return min(abs(record[left] - i), abs(record[right] - i))
                
        
                