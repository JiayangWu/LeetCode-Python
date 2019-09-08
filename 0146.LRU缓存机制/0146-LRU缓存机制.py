class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        self.capacity = capacity
        self.record = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.record:
            tmp = self.record.pop(key)
            self.record[key] = tmp
            return tmp
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.record:
            self.record.pop(key)         
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.record.popitem(last = False)
        self.record[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)