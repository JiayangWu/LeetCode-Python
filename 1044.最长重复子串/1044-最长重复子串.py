class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = 0
        d = {}
        for i in range(len(S)):
            for j in range(i + 1, len(S)):
                # if i==j:
                #     continue
                if S[i] == S[j]:
                    d[(i,j)]=d.get((i-1,j-1),0)+1
                    ans=max(ans,d[(i,j)])
        # print d
        return ans