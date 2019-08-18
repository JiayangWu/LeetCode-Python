class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        record = dict()
        record[1] = ["0", "1", "8"]
        record[2] = ["11", "69", "88", "96"]
        pair = ["00", "11", "88", "69", "96"]
        if n <= 2:
            return record[n]
        cnt = 3
        while cnt <= n:
            tmp = []
            if (cnt - 1) % 2 == 0: #如果前一个是偶数长度，那么直接在中间加长度为1的就可以
                for item in record[cnt - 1]:
                    for num in record[1]:
                        tmp.append(item[:len(item)// 2] + num + item[len(item) // 2:])
            else:
                for item in record[cnt - 2]:
                    for num in pair:
                        tmp.append(item[:len(item)// 2] + num + item[len(item) // 2:])
            record[cnt] = tmp
            cnt += 1
        return record[n]
        