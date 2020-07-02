class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10 ** 9 + 7
        
        dp = [[[float("-inf"), 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] not in "XS":
                    
                    for dx, dy in [[0, 1], [1, 0], [1, 1]]:
                        if dp[i][j][0] < dp[i + dx][j + dy][0]:
                            dp[i][j] = [dp[i + dx][j + dy][0], 0]
                            
                        if dp[i][j][0] == dp[i + dx][j + dy][0]:
                            dp[i][j][1] += dp[i + dx][j + dy][1]
                            
                    dp[i][j][0] += int(board[i][j]) if board[i][j] != "E" else 0
                    
        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % MOD]
                    
        
                
        
        