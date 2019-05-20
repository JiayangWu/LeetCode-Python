class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen, repeat = set(), set()
        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in seen:
                repeat.add(temp)
            else:
                seen.add(temp)
                
        return list(repeat)