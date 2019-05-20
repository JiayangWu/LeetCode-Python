class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        record = dict()
        for i, char in enumerate(s):
            record[char] = record.get(char, 0) + 1
        
        odd_cnt = 0
        for key, val in record.items():
            if val % 2:
                odd_cnt += 1
                if odd_cnt > 1:
                    return False
        return True