class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ss, tt = [], []
        
        def helper(A, aa):
            for a in A:
                if a != '#':
                    aa.append(a)
                else:
                    if aa:
                        aa.pop()
        
        helper(S, ss)
        helper(T, tt)
        return ss==tt