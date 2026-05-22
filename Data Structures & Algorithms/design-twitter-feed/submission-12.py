class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time,tweetId])
        self.time -= 1
        if len(self.tweetMap[userId])>10:
            self.tweetMap[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap, minheap = [], []
        res = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId])>=10:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId])-1
                    time,tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxheap,[-time,tweetId,followeeId,index-1])
                    if len(maxheap)>10:
                        heapq.heappop(maxheap)
            while maxheap:
                time, tweetId, followeeId, index = heapq.heappop(maxheap)
                heapq.heappush(minheap,[-time, tweetId, followeeId, index])
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId])-1
                    time,tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minheap,[time,tweetId,followeeId,index-1])
        while minheap and len(res)<10:
             time, tweetId, followeeId, index = heapq.heappop(minheap)
             res.append(tweetId)
             if index>=0:
                time,tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [time, tweetId, followeeId, index-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followMap[followerId]:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
