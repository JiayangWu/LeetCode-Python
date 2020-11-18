import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()
        self.l = []

    def insert(self, val):
        """
        Ins
from typing import ValuesViewerts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.l.append(val)
            self.dic[val] = len(self.l) - 1
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
       
        if val not in self.dic:
            return False
        else:
            # get the index of the element to be delted
            index = self.dic[val]
            self.dic.pop(val)

            # swap the element with the last element
            self.l[index], self.l[-1] = self.l[-1], self.l[index]

            if index != len(self.l) - 1:
                # if swap happened, update the index of element that got swapped
                self.dic[self.l[index]] = index

            self.l.pop()

            return True
            


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return random.choice(self.l)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()