class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # O£¨N ^ 2£©
        record = collections.defaultdict(list)
        for i, word in enumerate(strings):
            tmp = tuple()
            for j in range(1, len(word)):
                num = ord(word[j]) - ord(word[j - 1])
                if num < 0:
                    num += 26
                tmp += (j, num)
            record[tmp].append(word)
            
        return record.values()