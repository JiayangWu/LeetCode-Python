class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        d = defaultdict(list)
        for word in strs:
            d["".join(sorted(word))].append(word)
        
        return [val for key, val in d.items()]