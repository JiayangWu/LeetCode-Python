class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        flatten = sum(mat,[])  
        dic = Counter(flatten)
        for num in mat[0]:
            if dic[num] == len(mat):
                return num
        return -1