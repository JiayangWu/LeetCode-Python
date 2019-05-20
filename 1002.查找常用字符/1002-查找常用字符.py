class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        compare = collections.Counter(A[0])  
        
        for i in A:
            compare &= collections.Counter(i)
                
        return list(compare.elements())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(A)
#         c = [collections.Counter(A[i]) for i in range(n)]
#         print c
        
#         ans = c[0]
#         for i in range(1, n):
#             for key in ans:
#                 ans[key] = min(ans[key], c[i][key])
                
#         res = list()
#         for key in ans:
#             for i in range(ans[key]):
#                 res.append(key)
#         return res