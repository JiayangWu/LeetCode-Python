class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """    
        pre = 1
        res = []
        for i, num in enumerate(target):
            if i == 0:
                res += (num - pre) * ["Push", "Pop"] + ["Push"]
            else:
                res += (num - pre - 1) * ["Push", "Pop"] + ["Push"]
            pre = num
        return res
                
#         i = 0 #index
#         j = 1 #num for num in range(1, n)
#         res = []
#         while i < len(target):
#             if target[i] == j:
#                 res += ["Push"]
#                 i += 1
#             else:
#                 res += ["Push", "Pop"]
#             j += 1
                
#         return res