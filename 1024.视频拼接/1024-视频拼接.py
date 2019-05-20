class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        #开头是0的必须选一个，结尾是T的必须选一个，这两个都选最长的。
        res = 1
        l = list()
        
        hashmap = dict()
        for clip in clips:
            hashmap[clip[0]] = max(hashmap.get(clip[0], 0),clip[1])
            
        
        start, end = 0, hashmap.get(0, 0)
        reach = end
        while(1):
            s, e = start, end
            if reach >= T:
                break
            for cnt in range(start + 1, end + 1):
                if hashmap.get(cnt, 0) > reach:
                    reach = hashmap.get(cnt, 0)
                    s = cnt
                    e = reach
                    
            if s == start and e == end:#没有变
                return -1
            start, end = s, e
            res += 1
            

        return res
        
        