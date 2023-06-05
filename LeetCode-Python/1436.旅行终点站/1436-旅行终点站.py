class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()

        src2des = {}
        for path in paths:
            src, des = path[0], path[1]
            cities.add(src)
            cities.add(des)

            src2des[src] = des

        for city in cities:
            if city not in src2des:
                return city