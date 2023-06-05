class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row, col = int(coordinates[1]), ord(coordinates[0]) - ord("a")
        # 0 for balck, 1 for white
        if col % 2 == 0:
            color = 0
        else:
            color = 1

        if row % 2 == 0:
            color = 1 - color
        return color == 1
            