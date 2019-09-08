class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        if endWord not in wordList:
            return 0
        wordList = set(wordList) #必备优化，不然超时
        
        res, forward, backward = 2, {beginWord}, {endWord}
        while forward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                
            next_level = set()
            for word in forward:
                for i in range(len(word)):
                    for k in range(26):
                        tmp = word[:i] + chr(ord("a") + k) + word[i + 1:]
                        
                        if tmp in backward: #找到了
                            return res
                        if tmp in wordList:
                            next_level.add(tmp)
                            wordList.remove(tmp)
            res += 1
            forward = next_level
                            
                        
        return 0