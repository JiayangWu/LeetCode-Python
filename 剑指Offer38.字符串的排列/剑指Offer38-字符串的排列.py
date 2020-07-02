class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from itertools import permutations
        res = []
        visited = set()
        for item in list(permutations(s)):
            s = "".join(item)
            if s not in visited:
                res.append(s)
                visited.add(s)

        return res