class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA, sumB, setB = sum(A), sum(B), set(B)
        x=(sumB - sumA)/2
        for v in A:
            if x + v in setB:
                return [v, x + v]