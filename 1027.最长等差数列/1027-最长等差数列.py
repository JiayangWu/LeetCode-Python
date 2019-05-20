class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #dp[i][d]表示以下标i结尾，公差为d的子序列的长度
        res = 1
        l = len(A)
        dp = [[1] * 20001 for j in range(l)]
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                d = A[i] - A[j]
                d += 10001
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)
                res = max(res, dp[i][d])
    
        return res
                    
# class Solution(object):
#     def longestArithSeqLength(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         def helper(A):
#             dp = [[1] * 20000 for i in range(len(A))]
#             ans = 1
#             for i in range(1, len(A)):
#                 for j in range(i-1, -1, -1):
#                     diff = A[i]-A[j]
#                     diff += 10000
#                     dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
#                     ans = max(ans, dp[i][diff])
#             return ans
#         return helper(A)