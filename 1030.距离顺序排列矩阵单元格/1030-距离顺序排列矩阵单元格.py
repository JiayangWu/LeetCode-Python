class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0 , -1, 1]
        
        res = [[r0, c0]]
        queue = res[:]
        visited = [[0 for i in range(101)] for j in range(101)]
        visited[r0][c0] = 1
        while(queue):
            next_queue = list()
            for node in queue:
                x0, y0 = node[0], node[1]
                
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    # print x, y
                    if x < 0 or x >= R:
                        continue
                    if y < 0 or y >= C:
                        continue
                    if visited[x][y] == 1:
                        continue
                    # print visited
                   
                    res.append([x,y])
                    visited[x][y] = 1
                    next_queue.append([x,y])
            queue = next_queue[:]
            # print queue, res
        
        return res
                