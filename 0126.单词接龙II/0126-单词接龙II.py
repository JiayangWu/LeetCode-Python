class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict, deque
        if endWord not in wordList:
            return []
        wordList = set(wordList)
        wordList.add(beginWord)
        
        record = defaultdict(set)
        flag, forward, backward = True, {beginWord}, {endWord}
        while forward:
            if len(forward) > len(backward):
                flag, forward, backward = not flag, backward, forward
            
            wordList -= forward
            next_level = set()
            for word in forward:
                for i in range(len(word)):
                    for k in range(26):
                        tmp = word[:i] + chr(ord("a") + k) + word[i + 1:]
                        
                        if tmp in wordList:
                            next_level.add(tmp)
                            if flag:
                                record[tmp].add(word)
                            else:
                                record[word].add(tmp)
                                
            if next_level & backward:#有交集说明找到了
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[x] + y for y in res for x in record[y[0]]]
                return res
            # res += 1
            forward = next_level
        return []      
                        
        return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        for word in wordList:
            wl.add(word)
            
        record = defaultdict(list)
        queue = deque()
        queue.append(endWord)
        # wl.remove(endWord)
        def bfs(queue):
            if not queue:
                return 
            next_queue = deque()
            while queue:
                cur = queue.popleft()
                print wl, cur
                
                for i in range(len(cur)):
                    for k in range(26):
                        tmp = cur[:i] + chr(ord("a") + k) + cur[i + 1:]

                        if tmp != cur and tmp in wl and tmp not in record[cur]:
                            
                            next_queue.append(tmp)
                            record[cur].append(tmp)
                wl.remove(cur)
        
            bfs(next_queue)

        bfs(queue)
        print record
        self.min_length = 2 ** 32 - 1
        self.res = []
        
        def dfs(bW, eW, path):
            if len(path) > self.min_length:
                return
            print path, eW, record[eW]
            if bW == eW:
                # if len(path) + 1 < self.min_length:
                #     self.res = [[eW] + path ]
                #     self.min_length = len(path) + 1
                # elif len(path) + 1 == self.min_length:
                self.res.append([eW] + path )
                return

            for pre_node in record[eW]:
                if pre_node not in visited:
                    visited.add(pre_node)
                    dfs(bW, pre_node, [eW] + path )
                    visited.remove(pre_node)
                
        visited = set()
        visited.add(endWord)
        dfs(beginWord, endWord, [])
        return self.res
                            