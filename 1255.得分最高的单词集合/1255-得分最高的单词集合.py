class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        from collections import defaultdict, Counter
        dic = dict()
        letter_dic = defaultdict(int)
        for i, val in enumerate(score):#构建一个字典
            dic[chr(ord("a") + i)] = val #key是 字母，val是字母对应的分数
            
        letter_dic = Counter(letters)#构建另一个字典， key是字母， val是每次字母剩余的个数
 
        s = set(letters)
        v_words = []
        for word in words:#删掉所有根本不可能被构成的单词
            flag = 0
            for char in word:
                if char not in s:
                    flag = 1
            if flag: # 如果一个单词里存在某个在letters里找不到的字母，则无需考虑这个单词
                continue
            v_words.append(word)
        self.res = 0
                
        def helper(word, letter_dic):
            # return True 如果word能用letter_dic里的letter构成，否则返回False
            dicc = collections.Counter(word)
            for key in dicc:
                if dicc[key] > letter_dic[key]:
                    return False
            return True
        
        def dfs(start, tmp):
            self.res = max(self.res, tmp)
            if start >= len(v_words):
                return
            
            for i in range(start, len(v_words)):#从start开始找，避免重复
                if helper(v_words[i], letter_dic):#如果当前单词可以被构成
                    for char in v_words[i]: #构成它，更新字典
                        letter_dic[char] -= 1
                    dfs(i + 1, tmp + sum([dic[char] for char in v_words[i]])) #dfs下一层
                    for char in v_words[i]: #回溯，复原所有状态
                        letter_dic[char] += 1                   
        dfs(0, 0)
        return self.res