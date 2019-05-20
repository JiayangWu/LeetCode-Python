class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k == len(matrix) ** 2:
            return matrix[-1][-1]
        l = list()
        count = 0
        for i in matrix:
            for j in i:
                l.append(j)
        l.sort()
        return l[k - 1]
       # print l
       #  for index,i in enumerate(l):
       #      if index < len(l) - 1 and l[index] != l[index+1]:
       #          count += 1
       #          print count
       #      if count == k:
       #          return l[i]