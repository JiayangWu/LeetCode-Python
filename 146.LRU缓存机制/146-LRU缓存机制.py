class Node(object):
    def __init__(self, key, value, nxt, prev):
        self.key = key
        self.value = value
        self.next = nxt
        self.prev = prev
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.record = dict()
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, self.head, self.head)
        self.head.next = self.tail
        self.head.prev = self.tail
        
    def move_to_end(self, key):
        node = self.record[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        prev_to_tail = self.tail.prev
        node.next = self.tail
        node.prev = prev_to_tail
        prev_to_tail.next = node
        self.tail.prev = node        
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key in self.record:
            self.move_to_end(key)
            return self.record[key].value
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.record:
            self.move_to_end(key)
            self.record[key].value = value
        else:
            if self.capacity == 0:
                self.record.pop(self.head.next.key)
                new_first_node = self.head.next.next
                self.head.next = new_first_node
                new_first_node.prev = self.head
            else:
                self.capacity -= 1
                
            prev_to_tail = self.tail.prev
            new_node = Node(key, value, self.tail, prev_to_tail)
            self.record[key] = new_node
            prev_to_tail.next = new_node
            self.tail.prev = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)