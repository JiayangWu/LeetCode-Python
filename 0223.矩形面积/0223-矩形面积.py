class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # [A, C]和[E, G]取交集, [B, D]和[F, H]取交集
        if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:
            S_overlap = 0
        else:
            S_overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        S_first_square = (D - B) * (C - A)
        S_second_square = (H - F) * (G - E)
        # print S_second_square, S_first_square, S_overlap
        return S_second_square + S_first_square - S_overlap