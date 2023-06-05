class Solution:
    def oddString(self, words: List[str]) -> str:
        l = []
        for word in words:
            diff = []
            for i, char in enumerate(word):
                if i:
                    diff.append(ord(char) - ord(word[i - 1]))
            l.append(diff)
        # print(l)

        if l[0] != l[1] and l[0] != l[2]:
            return words[0]
        
        for i, diff in enumerate(l):
            if diff != l[0]:
                return words[i]