class ThroneInheritance(object):
    def __init__(self, kingName):
        """
        :type kingName: str
        """
        from collections import defaultdict
        self.par2child = defaultdict(list)
        self.kingName = kingName
        self.deaths = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.par2child[parentName].append(childName)


    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.deaths.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        return self.preorder(self.kingName)

    def preorder(self, cur):
        res = []
        if cur not in self.deaths:
            res.append(cur)

        for child in self.par2child[cur]:
            res += self.preorder(child)
        return res
        




# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()