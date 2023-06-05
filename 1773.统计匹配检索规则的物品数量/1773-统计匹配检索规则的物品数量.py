class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        key2index = {"type":0, "color":1, "name":2}
        for item in items:
            if item[key2index[ruleKey]] == ruleValue:
                res += 1
        return res
