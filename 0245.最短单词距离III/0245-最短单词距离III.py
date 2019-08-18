class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:       
            pre = -1
            res = float("inf")
            for i, word in enumerate(words):
                if word == word1:
                    if pre != -1:
                        res = min(res, i - pre)
                    pre = i
            return res        
        else:
            return self.previousSolution(words, word1, word2)
        
        
        
    def previousSolution(self, words, word1, word2):
        self.record = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.record[word].append(i)
        res = float("inf")
        p1, p2 = 0, 0
        list1, list2 = self.record[word1], self.record[word2]
        while p1 < len(list1) and p2 < len(list2):
            res = min(res, abs(list1[p1]- list2[p2]))
            if list1[p1] < list2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res