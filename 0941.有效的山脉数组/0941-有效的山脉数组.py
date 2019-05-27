class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False

        max_A_pos = A.index(max(A))
        if max_A_pos in [0, len(A) - 1]:
            return False
        
        first, last = A[:max_A_pos + 1], A[max_A_pos:]
        if len(first) != len(set(first)) or len(last) != len(set(last)):
            return False
        return first == sorted(first) and last == sorted(last)[::-1]
