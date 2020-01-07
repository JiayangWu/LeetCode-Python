class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # a = sorted(A)
        # if a == A or a[::-1] == A:
        #     return 0
        l, r = [0 for _ in A], [0 for _ in A]

        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                l[i] = l[i - 1] + 1
        
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                r[i] = r[i + 1] + 1
        
        res = 0
        for i in range(len(A)):
            if l[i] and r[i] and l[i] + r[i] > 1:
                res = max(l[i] + r[i] + 1, res)
        return res