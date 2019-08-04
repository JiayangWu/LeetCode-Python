class SnapshotArray(object):
    from collections import defaultdict
    def __init__(self, length):
        """
        :type length: int
        """
        self.history = dict()
        self.snap_id = -1
        self.history[self.snap_id] = dict()
    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.history[self.snap_id][index] = val

    def snap(self):
        """
        :rtype: int
        """
        import copy
        
        self.snap_id += 1
        self.history[self.snap_id] = copy.deepcopy( self.history[self.snap_id - 1])
        return self.snap_id

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        snap_id -= 1
        if index in self.history[snap_id]:
            return self.history[snap_id][index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)