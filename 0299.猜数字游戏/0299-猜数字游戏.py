class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import Counter
        dic_s = Counter(secret)
        dic_g = Counter(guess)
        
        a, b = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                dic_s[secret[i]] -= 1
                dic_g[secret[i]] -= 1
                
        for i in dic_s & dic_g:
            b += min(dic_s[i], dic_g[i])
            
        return "{}A{}B".format(a, b)