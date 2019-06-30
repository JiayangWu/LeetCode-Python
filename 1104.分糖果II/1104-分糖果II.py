class Solution(object):
    def distributeCandies(self, candies, n):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0 for _ in range(n)]
        multi = 0
        while candies > 0:
            for i in range(len(res)):
                distri = i + 1 + multi * n
                if candies > distri:
                    res[i] += distri
                    candies -= distri
                else:
                    res[i] += candies
                    candies = 0
                    break
            multi += 1
        return res