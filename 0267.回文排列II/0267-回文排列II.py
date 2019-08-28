class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or not self.canPermutePalindrome(s):
            return []
        if len(set(s)) == 1:
            return [s]
        xor = s[0]
        dic = collections.Counter(s)
        
        news = ""
        special = ""
        for key, val in dic.items():
            if val % 2:
                special = key
                val -= 1
            news += key * (val // 2)
        # print news
        res = set()
        def permutations(word, tmp):
            if not word:
                res.add(tmp + special + tmp[::-1])
            
            for i, char in enumerate(word):
                permutations(word[:i] + word[i + 1:], tmp + char)
        permutations(news, "")
        return list(res)
                
        
        
        
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        dic = collections.Counter(s)
        
        for key, val in dic.items():
            if val % 2:
                if not flag:
                    flag = 1
                else:
                    return False
        
        return True