import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digit = [i for i in range(1, n + 1)] #生成1 ~ n的列表
        res = ""
        while n > 0:
            tmp = math.factorial(n - 1) #计算一共有多少种组合
            idx =  (k - 1) / tmp #由K在tmp中占的比例来确定第一位的数字
            k -= idx * tmp #第一位确定之后，刷新k
            res += str(digit[idx])
            digit.pop(idx)
            n -= 1
        return res