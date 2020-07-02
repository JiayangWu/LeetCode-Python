class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        dic = defaultdict(set)
        res = 0
        usedrow = set()
        for row, seat in reservedSeats:
            dic[row].add(seat)
            usedrow.add(row)
        
        for row in usedrow:
            twothree = 2 not in dic[row] and 3 not in dic[row]
            fourfive = 4 not in dic[row] and 5 not in dic[row]
            sixseven = 6 not in dic[row] and 7 not in dic[row]
            eightnine = 8 not in dic[row] and 9 not in dic[row]

            if twothree and fourfive and sixseven and eightnine:
                res += 2
            elif twothree and fourfive:
                res += 1
            elif fourfive and sixseven:
                res += 1
            elif sixseven and eightnine:
                res += 1
        return res + (n - len(usedrow)) * 2
            