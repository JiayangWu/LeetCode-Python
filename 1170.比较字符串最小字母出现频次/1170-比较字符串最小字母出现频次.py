class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(word):
            return word.count(min(word))
        
        f_words = sorted([f(word) for word in words])
        
        res = []
        # print f_words
        for q in queries:
            cnt = f(q)
            # print(bisect.bisect(f_words, cnt))
            res.append(len(f_words) - bisect.bisect(f_words, cnt))
            
        return res
            
            