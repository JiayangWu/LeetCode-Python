class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        if not initialBoxes:
            return 0
        
        # boxes = set(initialBoxes)
        owned_keys = set()
        from collections import deque
        queue = deque(initialBoxes)
        res = 0
        record = dict()
        while queue:
            cur = queue.popleft()
            # print cur
            if status[cur] or cur in owned_keys: # This box could be opened
                for key in keys[cur]:
                    owned_keys.add(key)
                for box in containedBoxes[cur]:
                    queue.append(box)
                res += candies[cur]
            else:
                if cur in record and record[cur] == owned_keys:
                    break
                queue.append(cur)
                record[cur] = owned_keys
        return res