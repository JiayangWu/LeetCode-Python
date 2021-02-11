class DLLNode(object):
    def __init__(self, key, val, pre, nxt):
        self.key = key
        self.val = val 
        self.pre = pre 
        self.nxt = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = DLLNode(-1, -1, None, None)
        self.tail = DLLNode(-1, -1, self.head, None)
        self.head.next = self.tail 
        self.dic = dict() 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            value = self.dic[key].val
            self.moveToHead(self.dic[key])
            return value 

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dic:
            node = DLLNode(key, value, None, None)
            self.dic[key] = node
            if self.size < self.capacity:
                self.size += 1
            else:
                self.removeLastElement()
            self.insertToHead(node)
        else:
            self.dic[key].val = value
            self.moveToHead(self.dic[key])

    def insertToHead(self, node):

        pre_first = self.head.next
        self.head.next = node
        node.pre = self.head 
        pre_first.pre = node 
        node.next = pre_first
        
        # print (node.key, node.pre.key, node.next.key)

    def removeLastElement(self):
        pre_last = self.tail.pre 
        pre_second_last = pre_last.pre
        pre_second_last.next = self.tail
        self.tail.pre = pre_second_last
        self.dic.pop(pre_last.key)
    
    def moveToHead(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        self.insertToHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)