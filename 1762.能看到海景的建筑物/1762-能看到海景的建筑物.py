class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                last_index = stack[-1]
                stack.pop()
            stack.append(i)
        return sorted(stack)