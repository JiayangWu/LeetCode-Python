class Solution(object):
    def uncommonFromSentences(self, A, B):
        from collections import defaultdict
        count = defaultdict(int)
        for word in A.split():
            count[word] += 1
        for word in B.split():
            count[word] += 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]