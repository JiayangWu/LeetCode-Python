class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        
        for key in r:
            if m.get(key, 0):
                if m[key] < r[key]:
                    return False
            else:
                return False
            
        return True