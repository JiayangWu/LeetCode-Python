class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [16]
        for num in arr:
            while stack and stack[-1] < num:
                res += stack.pop() * min(stack[-1], num)
            stack.append(num)
        
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res