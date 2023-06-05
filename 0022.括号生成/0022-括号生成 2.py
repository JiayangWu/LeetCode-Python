class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        
        def dfs(tmp, left, right):
            if len(tmp) == 2 * n:
                res.append(tmp)
                
            if left:
                dfs(tmp + "(", left - 1, right)
            if right > left:
                dfs(tmp + ")", left, right - 1)
                    
            
        dfs("", n, n)
        return res
        