class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, idd, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        from collections import deque,defaultdict
        # 1. find all k-level friends by BFS
        queue = deque([idd])
        visited = set([idd])
        for l in range(level):
            friendset = set()
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for fri in friends[cur]:
                    if fri not in visited:
                        visited.add(fri)
                        queue.append(fri)

        # 2. find watched videos of all k-level friends
        videos = defaultdict(int)
        for friend in queue:
            for video in watchedVideos[friend]:
                videos[video] += 1

        # 3. count the frequency
        res = [[key, val] for key, val in videos.items()]
        res = sorted(res, key = lambda x:(x[1], x[0]))
        
        return [x[0] for x in res]