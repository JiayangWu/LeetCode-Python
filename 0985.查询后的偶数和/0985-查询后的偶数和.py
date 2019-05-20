class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sumOfEven = sum(num for num in A if  not num % 2)
        result = []
        
        for item in queries:
            value = item[0]
            index = item[1]
            newvalue = A[index] + value
            
            if not A[index] % 2 and not newvalue % 2: # even and even
                sumOfEven += value
            elif not A[index] % 2 and newvalue % 2:  # even and odd
                sumOfEven -= A[index] 
            elif A[index] % 2 and not newvalue % 2:  # odd and even
                sumOfEven += newvalue
                
            result.append(sumOfEven)            
            A[index] = newvalue
            
        return result
            