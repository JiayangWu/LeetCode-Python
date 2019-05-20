# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """        
        i, j = 0, 0
        res = list()
        while(i < len(A) and j < len(B)):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            
            if start <= end:
                res.append([start, end])
                
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
                                

                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         la,lb = A[-1][1], B[-1][1]
#         dica, dicb = dict(), dict()
#         for i in A:
#             for j in range(i[0],i[1] + 1):
#                 dica[j] = 1
                
#         for i in B:
#             for j in range(i[0], i[1] + 1):
#                 dicb[j] = 1
        
#         res = list()
#         i = 0
#         while(i <= max(la, lb)):
#             print dica.get(i, 0), dicb.get(i, 0)
#             if dica.get(i,0) and dicb.get(i,0):#重叠开始
#                 start = i
#                 while(dica.get(i,0) and dicb.get(i, 0)): #没有考虑区间，而是单纯地考虑了点
#                     i +=1
#                 res.append([start, i - 1])
#             i += 1
        
#         return res
                
                
                