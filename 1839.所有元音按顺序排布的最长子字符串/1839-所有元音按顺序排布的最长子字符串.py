class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        sequence = {"a":1, "e":2, "i":3, "o":4, "u":5}

        last_vowel = None
        res = 0
        start = 0
        cur_set = set()
        for i, ch in enumerate(word):
            if not i or sequence[last_vowel] > sequence[ch]:
                start = i
                cur_set = set(ch)
            else:
                cur_set.add(ch)
            # print(cur_set)
            if ch == "u" and len(cur_set) == 5:
                res = max(res, i - start + 1)
            last_vowel = ch
        return res
