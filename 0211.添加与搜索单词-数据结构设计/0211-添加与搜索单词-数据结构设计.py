class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.roots = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        print word
        node = self.roots
        for char in word:
            node = node.setdefault(char, {})
        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        self.res = False
        self.searchHelper(self.roots, word)
        return self.res

    def searchHelper(self, dic, word):
        if not word:
            self.res |= "end" in dic
            return
        node = dic
        i, char = 0, word[0]
        if char == ".":#È«Æ¥Åä
            for x in "abcedfghijklmnopqrstuvwxyz":
                if x in node:
                    self.searchHelper(node[x], word[1:])
        elif char in node:
            self.searchHelper(node[char], word[1:])
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)