class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)