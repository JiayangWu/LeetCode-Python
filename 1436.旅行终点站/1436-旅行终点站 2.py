class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        return (set(pair[1] for pair in paths) - set(pair[0] for pair in paths)).pop()