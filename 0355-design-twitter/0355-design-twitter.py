class Twitter:

    def __init__(self):
        self.count = 0
        self.postMap = collections.defaultdict(list)
        self.followMap = collections.defaultdict(set)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([self.count,tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.followMap[userId].add(userId)
        minHeap = []
        following = self.followMap[userId]
        for user in following:
            userPost = self.postMap[user]
            posts = userPost[:11]
            for post in posts:
                minHeap.append(post)
        heapq.heapify(minHeap)
        k = 0
        while minHeap and k < 10:
            count,tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
            k+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)