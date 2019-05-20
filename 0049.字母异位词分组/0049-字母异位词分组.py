class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = dict()
        for s in strs:
            t = "".join(sorted(s))

            if t in hashmap:
                hashmap[t].append(s)
            else:
                hashmap[t] = [s]
            
        return hashmap.values()