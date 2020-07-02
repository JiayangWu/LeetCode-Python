class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.use = {}  # 使用的频率
        self.cache = {}  # 值
        self.size = capacity
        self.arr = []  # 确保频率一样时，删除最近没有使用

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.use[key] += 1
            self.arr.remove(key)
            self.arr.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.use[key] += 1
            self.arr.remove(key)
            self.arr.append(key)
        else:
            if len(self.cache) < self.size:
                self.cache[key] = value
                self.use[key] = 1
                self.arr.append(key)
            else:
                if self.use:
                    v = min(self.use.values())
                    lost = -1
                    for x in self.arr:
                        if self.use[x] == v:
                            lost = x
                            break
                    self.cache.pop(lost)
                    self.use.pop(lost)
                    self.arr.remove(lost)
                    self.cache[key] = value
                    self.use[key] = 1
                    self.arr.append(key)        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)