class Solution(object):
    def generate(self, temp, left, right, result):
        if (left == 0 and right == 0):
            result.append(temp)
            return
        if (left > 0):
            self.generate(temp + "(", left-1, right, result)
        if (left < right):
            self.generate(temp + ")", left, right - 1, result)
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate("", n, n, result)
        return result
    

            
        
        