class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        prefix = ""
        for char in searchWord:
            tmp = []
            prefix += char
            idx = bisect.bisect_left(products, prefix) # 找当前prefix 起点，因为有序所以二分
            for word in products[idx:]:
                if len(tmp) >= 3 or word[:len(prefix)] > prefix:
                    break
                if word[:len(prefix)] == prefix:
                    tmp.append(word)
            res.append(tmp)
        return res