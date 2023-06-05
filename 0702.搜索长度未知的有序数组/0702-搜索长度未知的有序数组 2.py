class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i = 0
        tmp = reader.get(i)
        if tmp > target: #target比第一个元素都小，所以不存在
            return -1
        while tmp != 2147483647:
            if tmp == target: #找到了
                return i
            if tmp > target: #后面的元素都比target大，找不到
                break
            i += 1
            tmp = reader.get(i)
        return -1 