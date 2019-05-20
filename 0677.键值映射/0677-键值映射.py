class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.data[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for key, val in self.data.items():
            if key.startswith(prefix):
                res += val
                
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)