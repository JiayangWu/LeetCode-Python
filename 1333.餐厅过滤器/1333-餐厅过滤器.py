class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        if not restaurants:
            return []
        
        res = []
        for i, rating, vF, mP, mD in restaurants:
            if not veganFriendly or (vF and veganFriendly):
                if mP <= maxPrice and mD <= maxDistance:
                    res.append([i, rating])

        return [i for i, rating in sorted(res, key = lambda x:(x[1], x[0]), reverse = True)]