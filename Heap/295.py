class MedianFinder:
    
    def __init__(self):
        self.hi = []
        self.lo = []

    def addNum(self, num: int) -> None:
        heappush(self.hi, -num)
        heappush(self.lo, -heappop(self.hi))
        if len(self.lo) > len(self.hi):
           heappush(self.hi, -heappop(self.lo)) 

    def findMedian(self) -> float:
        if len(self.hi) > len(self.lo):
            return -self.hi[0]
        else:
            return  (-self.hi[0]+self.lo[0]) /2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()