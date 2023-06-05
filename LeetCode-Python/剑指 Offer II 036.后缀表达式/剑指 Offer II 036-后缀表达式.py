import math
class Solution:    
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        res = 0
        for token in tokens:
            # print(num_stack)
            if token[-1].isdigit():
                num_stack.append(int(token))
            else:
                second, first = num_stack.pop(), num_stack.pop()
                if token == "+":
                    num_stack.append(first + second)
                elif token == "-":
                    num_stack.append(first - second)
                elif token == "*":
                    num_stack.append(first * second)
                elif token == "/":
                    num_stack.append(int(first / second))

        return num_stack[0]