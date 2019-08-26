from heapq import *
class DinnerPlates(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.stack = []
        self.c = capacity
        self.idx = [] #用于存放有空位的栈的下标

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.idx:
            index = heappop(self.idx) #找最小的空的栈的下标
            self.stack[index].append(val) #插入val
            if len(self.stack[index]) < self.c: #如果插了之后还没满，就把这个空的栈的下标放进self.idx
                heappush(self.idx, index)
        else: #现在所有栈都满了，只能新增一个栈在末尾
            self.stack.append([val])
            if self.c > 1:
                self.idx.append(len(self.stack) - 1)
            

    def pop(self):
        """
        :rtype: int
        """
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        if not self.stack: #所有的栈都是空的
            return -1
        else:
            if len(self.stack[-1]) == self.c: #如果本来是满的栈
                heappush(self.idx, len(self.stack) - 1) #现在要变成有空位的栈了
            return self.stack[-1].pop()
            
    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stack): #下标越界
            return -1
        else:
            s = self.stack[index] # 把下标为index的栈取出来
            if len(s) == self.c: #如果这个栈本来是满的
                heappush(self.idx, index) #马上要变空了
            return s.pop() if s else -1 #如果这个栈是空的，返回-1， 否则返回pop


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)