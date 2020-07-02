class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [] #发推记录
        self.f = {} #记录每个人关注了谁
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.stack.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        out = []
        following = [userId]
        if userId in self.f:
            following += self.f[userId]
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] in following:
                out.append(self.stack[i][1])
            if len(out) == 10:
                return out
        return out
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.f:
            self.f[followerId] = [followeeId]
        else:
            if followeeId not in self.f[followerId]:
                self.f[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.f:
            if followeeId in self.f[followerId]:
                self.f[followerId].remove(followeeId)