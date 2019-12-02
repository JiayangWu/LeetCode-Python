class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        grid = [[-1 for _ in range(3)] for _ in range(3)]
        def check():
            for row in grid:
                if row == [0, 0, 0]:
                    return 0
                if row == [1, 1, 1]:
                    return 1

            for j in range(3):
                tmp = []
                for i in range(3):
                    tmp.append(grid[i][j])
                if tmp == [0, 0, 0]:
                    return 0
                if tmp == [1, 1, 1]:
                    return 1                

            tmp = [grid[0][0], grid[1][1], grid[2][2]]
            if tmp == [0, 0, 0]:
                return 0
            if tmp == [1, 1, 1]:
                return 1      

            tmp = [grid[2][0], grid[1][1], grid[0][2]]
            if tmp == [0, 0, 0]:
                return 0
            if tmp == [1, 1, 1]:
                return 1  
            return -1
        

        player = 0
        for move in moves:
            grid[move[0]][move[1]] = player
            player = 1 - player
            
            tmp = check()
            if tmp != -1:
                return "A" if tmp == 0 else "B"
        return "Draw" if len(moves) == 9 else "Pending"
        
       