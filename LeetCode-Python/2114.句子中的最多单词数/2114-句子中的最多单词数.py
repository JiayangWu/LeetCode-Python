class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for sentence in sentences:
            word_count = len(sentence.split())
            res = max(res, word_count)
        return res