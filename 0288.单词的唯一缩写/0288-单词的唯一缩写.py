class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.dic = defaultdict(list)
        for word in dictionary:
            if len(word) <= 2:
                self.dic[word].append(word)
            else:
                self.dic[word[0] + str(len(word) - 2) + word[-1]].append(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            return not self.dic[word] or self.dic[word] == [word] * len(self.dic[word])
        else:
            s = word[0] + str(len(word) - 2) + word[-1]
            return  not self.dic[s] or self.dic[s] == [word] * len(self.dic[s])
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)