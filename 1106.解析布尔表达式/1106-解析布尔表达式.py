class Solution(object):
    def parseBoolExpr(self, exp):
        """
        :type expression: str
        :rtype: bool
        """
        symbol = []
        stack = []
        op = ["|", "&", "!"]
        
        for c in exp:
            if c == "t":
                stack.append(True)
            elif c == "f":
                stack.append(False)
            elif c in op:
                symbol.append(c)
            elif c == ",":
                continue
            elif c == "(":
                stack.append(c)
            else:
                o = symbol.pop()
                tmp = stack[-1]
                while stack and stack[-1] != "(":
                    if o == "|":
                        tmp |= stack.pop()
                    elif o == "&":
                        tmp &= stack.pop()
                    else:
                        tmp = not stack.pop()
                stack.pop()
                stack.append(tmp)
        # print stack
        return stack[0]