class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = ["" for _ in s]

        for i, char in enumerate(s):
            l[indices[i]] = char
        return "".join(l)