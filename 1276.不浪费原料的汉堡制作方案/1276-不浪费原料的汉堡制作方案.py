class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        doublex = tomatoSlices - cheeseSlices * 2
        if doublex < 0 or doublex % 2 != 0:
            return []
        
        x = doublex // 2
        y = cheeseSlices - doublex // 2
        if x >= 0 and y >= 0:
            return [x, y]
        return []