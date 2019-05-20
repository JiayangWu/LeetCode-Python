class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        res = []
        for digit in digits:
            temp = []
            n = int(digit)
            for char in mapping[n]:
                # print char
                if not res:
                    temp.append(char)
                else:
                    for item in res:
                        temp.append(item + char)
            res = temp
            # print res
        
        return res