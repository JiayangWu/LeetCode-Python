class Solution:
    def compressString(self, S: str) -> str:
        res = ""
        index = 0
        while index < len(S):
            count = 1
            char = S[index]
            while index + 1 < len(S) and S[index] == S[index + 1]:
                index += 1
                count += 1
            res += char + str(count)
            index += 1
        
        return res if len(res) < len(S) else S