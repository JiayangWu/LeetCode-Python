class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        from collections import defaultdict
        dic = defaultdict(set)
        vocab = set()
        text = text.split()
        
        for w1, w2 in synonyms:
            dic[w1].add(w2)
            dic[w2].add(w1)
            vocab.add(w1)
            vocab.add(w2)

        self.res = []
        
        def generateList(word, res, visited):
            res.add(word)
            for w in dic[word]:
                if w not in visited:
                    visited.add(w)
                    generateList(w, res, visited)
            
            return res

            
        def dfs(start, tmp):
            if start >= len(text):
                self.res.append(tmp)
                return
            
            word = text[start]
            if word in vocab:
                l = set()
                visited = set()
                generateList(word, l, visited)
                for w in l:
                    if start > 0:
                        dfs(start + 1, tmp + " " + w)
                    else:
                        dfs(start + 1, w)
            else:
                if start > 0:
                    dfs(start + 1, tmp + " " + word)
                else:
                    dfs(start + 1, word)        
        dfs(0, "")
        self.res.sort()
        return self.res
                    
            
                