class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return sorted(range(1, n + 1), key = str)
#         res = []
       
#         def dfs(k):
#             if k > n:
#                 return
#             res.append(k)
            
#             for i in range(10):
#                 dfs(10 * k + i)
        
#         for i in range(1, 10):
#             dfs(i)
#         return res