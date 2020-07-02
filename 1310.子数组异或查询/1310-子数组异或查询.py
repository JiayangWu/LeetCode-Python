class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        prefix = [0 for _ in [0] + arr]
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        # print prefix
        res = []
        for l, r in queries:
            res.append(prefix[l] ^ prefix[r + 1])
        
        return res