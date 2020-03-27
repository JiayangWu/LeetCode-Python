class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b 
            return a
        return functools.reduce(gcd, collections.Counter(deck).values()) >= 2