class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        record = [-2 ** 31] * 8
        
        for i in range(len(arr1)):
            for k in range(8): #生成八种可能的结果
                t = 0
                if k & 1:
                    t += arr1[i]
                else:
                    t -= arr1[i]
                if k & 2:
                    t += arr2[i]
                else:
                    t -= arr2[i]
                if k & 4:
                    t += i
                else:
                    t -= i
                # print k, t
                record[k] = max(record[k], t)
        # print record
        res = 0    
        for k in range(8):
            # print k, ~k
            res = max(res, record[k] + record[-k-1]) #第一项和最后一项，第二项和倒数第二项，两项之和一定是满足表达式的
        return res
                
            