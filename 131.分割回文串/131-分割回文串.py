class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        def dfs(start, tmp):
            
            if start >= len(s):
                # print tmp
                res.append(tmp[:])
                return

            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring == substring[::-1]:
                    tmp.append(substring)
                    dfs(i + 1, tmp)
                    tmp.pop()
        dfs(0, [])
        return res