class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        
        key = [0 for i in range(0, n)]
        key[0] = 1
        queue = [0]
        while(queue):
            newqueue = list()
            for i in queue:
                for k in rooms[i]:
                    if key[k] == 0:
                        key[k] = 1
                        newqueue.append(k)
            queue = newqueue[:]
        
        return sum(key) == n
            