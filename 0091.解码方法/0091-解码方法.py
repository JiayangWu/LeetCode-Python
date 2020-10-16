class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        dp = [0]*(len(s) + 1) # dp[i] represents ways of s[:i + 1]
        dp[1] = dp[0] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 2] in ["1", "2"]:
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 2] == "1" or (s[i - 2] == "2" and "1" <= s[i - 1] <= "6"):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

        # dp = [0]*(len(s) + 1)
        # if s[0] == '0':
        #     return 0
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, len(s)+1):
        #     if s[i-1] == '0' :
        #         if s[i-2] in ['1', '2']:
        #             dp[i] = dp[i-2]
        #         else:
        #             return 0
        #     elif s[i-2] == '1' or (s[i-2] == '2' and '1' <= s[i-1] <= '6'):
        #         dp[i] = dp[i-1] + dp[i-2]
        #     else:
        #         dp[i] = dp[i-1]
        # return dp[-1]



