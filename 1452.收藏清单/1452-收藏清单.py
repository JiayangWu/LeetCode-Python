class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        s = [set(l) for l in favoriteCompanies]
        return [i for i, s1 in enumerate(s) if not any(s1 < s2 for s2 in s)]