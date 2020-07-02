class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        dic = dict()
        for i, x in enumerate(B):
            dic[x] = i
        
        return [dic[x] for x in A]