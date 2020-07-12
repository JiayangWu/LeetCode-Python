class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon[0])==0:
            return 1
        dungeon[-1][-1] = max(1,1-dungeon[-1][-1])
        # 边界
        for i in range(len(dungeon)-2,-1,-1):
            dungeon[i][-1] = max(1,dungeon[i+1][-1]-dungeon[i][-1])
        for j in range(len(dungeon[0])-2,-1,-1):
            dungeon[-1][j] = max(1,dungeon[-1][j+1]-dungeon[-1][j])

        for i in range(len(dungeon)-2,-1,-1):
            for j in range(len(dungeon[0])-2,-1,-1):
                dungeon[i][j] = max(1,min(dungeon[i][j+1]-dungeon[i][j],dungeon[i+1][j]-dungeon[i][j]))
        # print(dungeon)
        return dungeon[0][0]