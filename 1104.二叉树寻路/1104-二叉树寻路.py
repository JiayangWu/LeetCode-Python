class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        while label > 1:
            res.append(label)
            label >>= 1
            label = label ^(1 << (label.bit_length() - 1)) - 1
        return [1] + res[::-1]
