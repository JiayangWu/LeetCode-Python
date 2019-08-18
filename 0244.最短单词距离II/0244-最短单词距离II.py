class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.record = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.record[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float("inf")
        p1, p2 = 0, 0
        while p1 < len(self.record[word1]) and p2 < len(self.record[word2]):
            res = min(res, abs(self.record[word1][p1] - self.record[word2][p2]))
            if self.record[word1][p1] < self.record[word2][p2]:
                p1 += 1
            else:
                p2 += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)