class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(" ")
        if len(pattern) != len(s):
            return False
        record = [0 for i in range(0, 26)] #记录下pattern里每个字母出现的次数
        hashmap = dict()
        
        for i, word in enumerate(s):
            t = ord(pattern[i]) - ord("a")
            
            if word not in hashmap.keys():
                if record[t] > 0:
                    return False
                hashmap[word] = pattern[i]
                record[t] = 1
            else:
                if hashmap[word] != pattern[i]:
                    return False
                
        return True
                
            
        