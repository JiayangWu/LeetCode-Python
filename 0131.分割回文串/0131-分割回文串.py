class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l, res = len(s), list()

        def dfs(start, tmp):
            if start >= l:
                res.append(tmp[:])
                
            for i in range(start, l):
                substring = s[start:i + 1]
                if substring == substring[::-1]: #子串是回文串
                    tmp.append(substring)
                    dfs(i + 1, tmp)
                    tmp.pop()
                    
        dfs(0, list())
        return res