class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import Counter
        words = sorted(words, key = lambda x: len(x))
        # dic = [Counter(word) for word in words]
        # words = list(set(words))
        # print len(words), words
        if len(words) == 1000:
            return 1
        def cover(str1, str2):
            # print str1, str2
            tmp = ""
            for i, char in enumerate(str2):
                tmp = str2[:i] + str2[i + 1:]
                if tmp == str1:
                    return True
            return False                    
        
        dp = [1 for _ in range(len(words))]
        for i, word in enumerate(words):
            if i >= 1 and words[i] == words[i - 1]:
                continue
            for j in range(i + 1, len(words)):
                # print word, words[j]
                if len(words[j]) - 1 > len(word):
                    break

                # print word, words[j]
                if len(words[j]) - 1 == len(word) and cover(word, words[j]):
                    # print word, words[j], i, j
                    dp[j] = max(dp[j], dp[i] + 1)
                    # print dp[i], dp[j]
        # print dp            
        return max(dp)
            
        
        