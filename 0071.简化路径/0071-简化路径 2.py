class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split("/")
        stack = []
        for item in l:
            if item != "." and item != ".." and item:
                stack.append(item)
            elif item == ".." and stack:
                stack.pop()

        return "/" + "/".join(stack)