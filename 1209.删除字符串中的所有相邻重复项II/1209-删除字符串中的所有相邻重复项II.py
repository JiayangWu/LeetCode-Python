class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for ch in s:
            if not stack:
                stack.append([ch, 1])
            else:
                if stack[-1][0] == ch:
                    stack[-1][1] += 1
                    if stack[-1][1] % k == 0:
                        stack.pop()
                else:
                    stack.append([ch, 1])

        return "".join(ch * freq for ch, freq in stack)