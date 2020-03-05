class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0 for _ in range(num_people)]
        cnt = 1
        while candies:
            for i in range(num_people):
                if candies >= cnt:
                    res[i] += cnt 
                    candies -= cnt 
                    cnt += 1
                else:
                    res[i] += candies 
                    candies = 0
                    break 
        return res