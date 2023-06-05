class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # store index into this stack
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last_index = stack[-1]
                res[last_index] = i - last_index
                stack.pop()
            stack.append(i)
        return res