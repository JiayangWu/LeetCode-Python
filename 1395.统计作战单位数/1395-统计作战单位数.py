class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        from collections import defaultdict
        
        
        def helper(rating):
            dic = defaultdict(int)
            res = 0
            
            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    if rating[j] > rating[i]:
                        dic[i] += 1


            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    if rating[j] > rating[i]:
                        res += dic[j]
            return res
        
        return helper(rating) + helper(rating[::-1])
