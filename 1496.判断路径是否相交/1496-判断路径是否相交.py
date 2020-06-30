class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        s = set([(0, 0)])
        x, y = 0, 0
        for d in path:
            if d == "N":
                y += 1
            elif d == "S":
                y -= 1
            elif d == "E":
                x += 1
            elif d == "W":
                x -= 1
            if (x, y) in s:
                return True
            s.add((x, y))
        return False
                