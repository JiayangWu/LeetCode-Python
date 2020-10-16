class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import deque
        wordDict = set(wordDict)
        record = [0]

        for i in range(len(s) + 1):
            for j in record:
                if s[j:i] in wordDict:
                    record.append(i)
                    break
        # print (record)
        return record[-1] == len(s)