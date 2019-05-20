class Solution(object):
    def leastBricks(self, walls):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        mark = {}
        for wall in walls:
            s = 0
            for i in xrange(len(wall) - 1):
                s += wall[i]
                mark[s] = mark.get(s, 0) + 1
        if not mark:
            return len(walls)
        #print(mark)
        return len(walls) - max(mark.values())