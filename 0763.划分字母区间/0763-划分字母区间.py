class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        
        for index, char in enumerate(S):
            dic[char] = index
        
        right = dic[S[0]]
        left = 0
        res = []
        for index, char in enumerate(S):
            right = max(right, dic[char])
            if index >= right:
                res.append(right - left + 1)
                left = right + 1
        
        return res
                
        
        
            
        