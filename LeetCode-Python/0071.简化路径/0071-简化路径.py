class Solution:
    def simplifyPath(self, path: str) -> str:
        path_names = path.split("/")
        stack = []
        for path_name in path_names:
            if path_name:
                if path_name == "..":
                    if stack:
                        stack.pop()
                elif path_name != ".":
                    stack.append(path_name)

        return  "/" + "/".join(stack)