class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        record = {}
        for word in words:
            if record.get(len(word), -1) == -1:
                record[len(word)] = [word]
            else:
                record[len(word)].append(word)
        # min_l, max_l = min(record.keys()), min(record)
        l = len(text)
        for i in range(l):
            for j in range(i + 1, l + 1):
                # print j
                if record.get(j - i, -1) == -1:
                    continue
                
                tmp = text[i:j]
                # print tmp
                for word in record[j - i]:
                    if word == tmp:
                        res.append([i, j - 1])
                        # flag = 1
                        break
                        
        return res
                        
                
                