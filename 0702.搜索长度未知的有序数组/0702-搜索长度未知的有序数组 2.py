class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i = 0
        tmp = reader.get(i)
        if tmp > target: #target�ȵ�һ��Ԫ�ض�С�����Բ�����
            return -1
        while tmp != 2147483647:
            if tmp == target: #�ҵ���
                return i
            if tmp > target: #�����Ԫ�ض���target���Ҳ���
                break
            i += 1
            tmp = reader.get(i)
        return -1 