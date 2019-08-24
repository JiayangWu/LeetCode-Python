class FileSystem(object):

    def __init__(self):
        self.dic = dict()

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path in self.dic: 
            return False
        parent = path.split("/")
        parent_path = ""
        for i in range(1, len(parent) - 1):
            # print parent, i
            parent_path += "/" + parent[i]
            # print parent_path
            if parent_path not in self.dic:
                return False
        self.dic[path] = value
        return True
        

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        return self.dic[path] if path in self.dic else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)