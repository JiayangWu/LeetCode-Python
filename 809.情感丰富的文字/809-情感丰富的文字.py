class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        
        s = set(S)
        res = 0
        for word in words:
            if len(S) < len(word):
                continue
                
            i, j = 0, 0
            flag = 0
            while i < len(S) and j < len(word):
                if S[i] != word[j]:
                    flag = 1
                    break
                pre = S[i]
                cnt_i = 0
                while i < len(S) and S[i] == pre:
                    i += 1
                    cnt_i += 1
                
                cnt_j = 0
                while j < len(word) and word[j] == pre:
                    j += 1
                    cnt_j += 1
                
                # print cnt_i, cnt_j
                if (cnt_i < 3 and cnt_i != cnt_j) or cnt_i < cnt_j:
                    flag = 1
                
            if not flag and i == len(S):
                res += 1
        return res