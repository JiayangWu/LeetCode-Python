class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.char_cnt = 0 # 统计 a - z 字符个数
        self.word_cnt = 0 # 统计结尾符 # 个数
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word: # word 入树
            node = node.setdefault(char, {})

        if not node: # not node 就代表当前 word 不是之前某一 word 的后缀        
            self.word_cnt += 1 
            self.char_cnt += len(word)
        node["end"] = True 

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ttree = Trie()

        for word in sorted(words, key = lambda x:len(x), reverse = True):
            # 按长度由大到小排序，再将每个 word 反向插入树
            ttree.insert(word[::-1])
        # print ttree.char_cnt, ttree.word_cnt
        return ttree.char_cnt + ttree.word_cnt