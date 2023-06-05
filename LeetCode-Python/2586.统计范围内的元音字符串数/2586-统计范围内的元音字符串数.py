class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowelStringCount = [0 for _ in words]
        VOWELS = set("aeiou")
        for i in range(len(words)):
            if words[i][0] in VOWELS and words[i][-1] in VOWELS:
                vowelStringCount[i] = vowelStringCount[i - 1] + 1
            else:
                vowelStringCount[i] = vowelStringCount[i - 1]

        res = []
        for l, r in queries:
            if l:
                res.append(vowelStringCount[r] - vowelStringCount[l - 1])
            else:
                res.append(vowelStringCount[r])
        return res
