class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alpha, digit = list(), list()
        for log in logs:
            if log.split(" ")[1][0].isdigit():
                 digit.append(log)
            else:
                alpha.append(log)        
        # print alpha
        alpha.sort(key = lambda x : x[x.index(" ") + 1:])
        
        return alpha + digit