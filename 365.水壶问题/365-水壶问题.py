class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if not z:
            return True
        if not x:
            return y == z
        if not y:
            return x == z
        if x + y < z:
            return False
        def gcd(a, b):
            while a % b:
                a, b = b, a % b
            return b
        return not z % gcd(x, y)