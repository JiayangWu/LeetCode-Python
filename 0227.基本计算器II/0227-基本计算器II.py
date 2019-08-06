import operator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        calculate = {
            "+": lambda x: res.append(x),
            "-": lambda x: res.append(-x),
            "*": lambda x: res.append(x * res.pop()),
            "/": lambda x: res.append(int(operator.truediv(res.pop(), x)))
        }
        op = "+"
        num = 0
        for char in s + "+":
            if char.isdigit():
                num = num * 10 + int(char)
            elif char != " ":
                calculate[op](num)
                op, num = char, 0
            # print res
        return sum(res)