class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.res,m,n = 0,len(board),len(board[0])

        def check(n):
            if n == 'B' or n == 'p':
                if n == 'p':self.res += 1
                return False
            return True
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'R':
                    for u in range(i-1,-1,-1):
                        if not check(board[u][j]):break                       
                    for d in range(i+1,m):
                        if not check(board[d][j]):break  
                    for l in range(j-1,-1,-1):
                        if not check(board[i][l]):break  
                    for r in range(j+1,n):
                        if not check(board[i][r]):break  
                    break
        return self.res

