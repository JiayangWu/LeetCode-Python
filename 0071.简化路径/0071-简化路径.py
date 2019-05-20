class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ""
        pathList = path.split("/")
        stack = []
        for path in pathList:
            if path == "." or path == "":
                continue
            if path == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(path)
        return "/" + "/".join(stack)