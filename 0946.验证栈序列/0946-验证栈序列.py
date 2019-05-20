class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)
            while(stack and popped[i] == stack[-1]):
                stack.pop()
                i += 1
        return stack == []
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        l = len(pushed)
        
        stack = list()

        
        for i in range(0, l):
            stack.append(pushed[i])
            while(stack and stack[-1] == popped[0]):
                stack = stack[:-1]
                popped = popped[1:]

        return stack == []

                
                
        