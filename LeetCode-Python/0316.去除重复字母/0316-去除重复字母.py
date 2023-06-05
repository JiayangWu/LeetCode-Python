class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        stack = [] # incresing stack
        for char in s:
            c[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and c[stack[-1]] >= 1:
                stack.pop()
            stack.append(char)
        return "".join(stack)