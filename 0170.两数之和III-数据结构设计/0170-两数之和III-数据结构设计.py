class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.dic = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.dic[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key, val in self.dic.items():
            if key * 2 == value:
                if val > 1:
                    return True
            else:
                if value - key in self.dic:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)