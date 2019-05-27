class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted(words, key = lambda x: -len(x))
        # print words
        from collections import Counter
        dic = [Counter(item) for item in words]
        # print dic
        res = 0
        l = len(words)
        for i in range(l - 1):
            for j in range(i + 1, l):
                # print i, j, dic[i] & dic[j]
                # if dic[i] & dic[j] == Counter():
                flag = 0
                for char in words[i]:
                    if char in dic[j]:
                        flag = 1
                        break
                if flag == 0:
                    res = max(res,  len(words[i]) *len(words[j]))
        return res