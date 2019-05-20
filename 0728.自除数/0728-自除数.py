class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
              
        res = list()
        for i in range(left, right + 1):
           
            flag = True
            n = i
            while(n):
                num = n % 10
                n //= 10
                if  not num or i % num != 0:
                    flag = False
                    break    
                    
            if flag:
                res.append(i)
                
        return res