#   """
#   This is the ImmutableListNode's API interface.
#   You should not implement it, or speculate about its implementation.
#   """
#   class ImmutableListNode(object):
#      def printValue(self): # print the value of this node.
# .        """
#          :rtype None
#          """
#
#      def getNext(self): # return the next node.
# .        """
#          :rtype ImmutableListNode
#          """

class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        if not head:
            return
        l = []
        p = head
        while p:
            l.append(p)
            p = p.getNext()

        while l:
            l.pop().printValue()
            