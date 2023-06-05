class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0

        for move in  moves:
            if move == "R":
                y += 1
            elif move == "L":
                y -= 1
            elif move == "U":
                x -= 1
            else:
                x += 1
        
        return [x, y] == [0, 0]