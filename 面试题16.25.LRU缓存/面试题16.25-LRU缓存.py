class DLLNode(object):
    def __init__(self, key, val, pre = None, next = None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1, self.head)
        self.head.next = self.tail
        self.dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            res = self.dic[key].val
            self.moveToHead(self.dic[key]) # set this node to be most recently used
            return res
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self.dic[key].val = value
            self.moveToHead(self.dic[key])
        else:
            node = DLLNode(key, value)
            self.dic[key] = node
            if self.size < self.capacity:
                self.size += 1
            else:
                self.removeLastNode()
            self.insertToHead(node)
        
    def insertToHead(self, node):
        pre_first = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = pre_first
        pre_first.pre = node

    def moveToHead(self, node):
        # 1. take it out
        node.pre.next = node.next
        node.next.pre = node.pre
        # 2. insert it to the head
        self.insertToHead(node)

    def removeLastNode(self):
        pre_last = self.tail.pre
        pre_second_last = pre_last.pre

        pre_second_last.next = self.tail
        self.tail.pre = pre_second_last

        self.dic.pop(pre_last.key)
                



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)