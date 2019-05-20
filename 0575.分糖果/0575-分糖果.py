class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #十个糖果，三种，要分五个，答案是三
        #八个糖果，八种， 要分四个，答案是四
        #十个糖果，六种，要分五个，答案是五
#         hashmap = dict()
#         for c in candies:
#             hashmap[c] = hashmap.get(c, 0) + 1
            
#         cnt = len(hashmap.keys())
        
        return min(len(set(candies)), len(candies)/ 2)