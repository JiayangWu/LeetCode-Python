class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        board = ["abcde", 
                 "fghij", 
                 "klmno", 
                 "pqrst", 
                 "uvwxy", 
                 "z"]
        
        dic = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                dic[board[i][j]] = [i, j]
                if i == 5:
                    break
         
        x0, y0 = 0,0
        res = ""
        for char in target:
            tmp = ""
            des = dic[char]         
            x1, y1 = des[0], des[1]
            if x0 == x1 and y0 == y1:
                res += "!"
                continue
            if x0 < x1:
                tmp += "D" * (x1 - x0)
            elif x0 > x1:
                tmp += "U" * (x0 - x1)
            if x1 == 5 and tmp and tmp[-1] == "D":
                tmp = tmp[:-1]
            if y0 < y1:
                tmp += "R" * (y1 - y0)
            elif y1 < y0:
                tmp += "L" * (y0 - y1)
            x0 = x1
            y0 = y1
            if x1 == 5:
                tmp += "D"
            tmp += "!"
            res += tmp
        return res
            
        
        