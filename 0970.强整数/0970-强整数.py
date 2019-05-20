class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        dpx = list()
        dpy = list()
        res = list()
        if x != 1:
            t = 0
            while( x **t < bound):
                dpx.append(x **t)
                t += 1
        else:
            dpx = [1]
        if y != 1:

            t = 0
            while(y **t < bound):
                dpy.append(y ** t)
                t += 1
        else:
            dpy = [1]

        for i, x in enumerate(dpx):
            for j, k in enumerate(dpy):
                t = x + k
                if t <= bound:
                    res.append(t)
        return list(set(res))