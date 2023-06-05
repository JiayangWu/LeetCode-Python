class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        steps = 0
        for log in logs:
            if log == "../" and steps:
                steps -= 1
            elif log not in ["../", "./"]:
                steps += 1
        return steps