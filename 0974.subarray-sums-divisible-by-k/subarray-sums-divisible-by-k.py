class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        s = [0 for i in range(len(A) + 1)] #s代表前缀和，即s[i]表示sum(A[:i])
        kcnt = [0 for i in range(K)] #k[i]代表s中有多少个元素 mod k 为i
        for i in range(len(A)):
            s[i + 1] = s[i] + A[i]
        for item in s:
            kcnt[item % K] += 1
        print s, kcnt
        #题目求连续子数组的和能被K整除，连续子数组的和就可以表示为前缀和的差
        #比如 sum(A[i:j + 1]) = s[j + 1] - s[i]
        #如果两个数的差能被K整除，就说明这两个数 mod k得到的结果相同
        #只要找有多少对 mod k 相同的数就可以得到结果
        #举例 对于[4,5,0,-2,-3,1] 5
        # s = [0, 4, 9, 9, 7, 4, 5] 
        # k = [2, 0, 1, 0, 4] 代表有s中有两个元素的余数都为0（即0和5），1个元素的余数为2（即7），四个元素的余数为4（即4994）
        # 所以在保证余数相同的情况下，取出两个数都可以得到一组答案。对于这个例子答案就是 C22 + C12 + C42 = 1 + 0 + 6 = 7
        return sum(x * (x - 1) // 2 for x in kcnt)
                