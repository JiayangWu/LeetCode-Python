class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        count = 0
        l = len(A)
        num = 0
        res = []
        while(num < l - 1):
            maxe = max(A)
            # print "max element is ", maxe
            index = A.index(maxe)
            # print index, num,res
            if index != l - num -1:
                res.append(index + 1)
                res.append(l-num)     
                B = A[:index + 1] #+ A[index + 1:]
                # print B
                B = B[::-1]
                B += A[index + 1:]
                # print B[::-1]
                A = B[::-1][:-1]
            else:
                # print A
                A = A[:-1]

            # print "A now is ", A
            num += 1
        return res
    