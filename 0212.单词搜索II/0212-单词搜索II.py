class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
            
        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "end" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        tree = Trie()
        for word in words:
            tree.insert(word)
        words = set(words)
        res = set()
        def dfs(x0, y0, node, tmpword):
            visited.add((x0, y0))
            # print tmpword, x0, y0
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and board[x][y] in node and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y, node[board[x][y]], tmpword + board[x][y])
                    visited.remove((x,y))
                    
            if tmpword in words:
                res.add(tmpword)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] in tree.root:
                    visited = set((i,j))
                    dfs(i, j, tree.root[board[i][j]], board[i][j])
        return list(res)
    