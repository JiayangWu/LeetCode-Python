class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            if item in ["+", "-", "*", "/"]:
                if item == "+":
                    temp = int(stack[-2]) + int(stack[-1])
                elif item == "-":
                    temp = int(stack[-2]) - int(stack[-1])
                    # print temp                
                elif item == "*":
                    temp = int(stack[-2]) * int(stack[-1])             
                elif item == "/":
                    temp = int(float(stack[-2])/ float(stack[-1]))                    
                stack.pop()
                stack.pop()
                stack.append(temp)
                
            else:
                stack.append(item)
                
        return int(stack[0])