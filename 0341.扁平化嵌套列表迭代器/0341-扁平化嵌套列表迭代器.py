# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        if nestedList:
            self.stack = nestedList[::-1]
        else:
            self.stack = []
    
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()
    
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            top = self.stack.pop()
            while not top.isInteger():
                self.stack += top.getList()[::-1]
                if self.stack:
                    top = self.stack.pop()
                else:
                    return False
            self.stack.append(top)
            return True
        else:
            return False
