class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        from collections import defaultdict
        dic = dict()
        for reg in regions:
            parent = reg[0]
            for child in reg[1:]: # 遍历所有的子区域
                dic[child] = (parent)

        ancestors_1 = set()
        while region1 in dic:
            ancestors_1.add(region1)
            region1 = dic[region1]
            
        while region2 not in ancestors_1 and region2 in dic:
            region2 = dic[region2]
            
        return region2