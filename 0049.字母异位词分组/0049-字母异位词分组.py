class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        record = dict()
        
        for word in strs:
            tmp = tuple(sorted(word))
            # print tmp
            if tmp in record:
                record[tmp].append(word)
            else:
                record[tmp] = [word]
        return [val for key, val in record.items()]
            
                