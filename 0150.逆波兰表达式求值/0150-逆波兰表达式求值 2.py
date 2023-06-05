class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i, x in enumerate(tokens):
            # print stack
            if x not in ["+", "-", "*", "/"]:
                stack.append(int(x))
            else:
                if x == "+":
                    tmp = stack[-1] + stack[-2]
                    stack = stack[:-2]       
                elif x == "-":
                    tmp = stack[-2] - stack[-1]
                    stack = stack[:-2]                    
                elif x == "*":
                    tmp = stack[-1] * stack[-2]
                    stack = stack[:-2]
                elif x == "/":
                    tmp = int( stack[-2] * 1.0 / stack[-1])
                    stack = stack[:-2]
                stack.append(tmp)
                
        return stack[0]