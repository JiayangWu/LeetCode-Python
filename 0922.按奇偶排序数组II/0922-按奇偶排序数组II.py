class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_pos = 1
        even_pos = 0
        while(1):
            while odd_pos < len(A) and A[odd_pos] % 2 == 1:
                odd_pos += 2
            while even_pos < len(A) and  A[even_pos] % 2 == 0 :
                even_pos += 2
            if even_pos >= len(A) and odd_pos >= len(A):
                break
            temp = A[even_pos]
            A[even_pos] = A[odd_pos]
            A[odd_pos] = temp
            # print A,odd_pos,even_pos
        return A
                
            