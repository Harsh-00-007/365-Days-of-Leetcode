import bisect

class RangeModule:

    def __init__(self):
        # Stores flat interval bounds: [left1, right1, left2, right2, ...]
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        # Find insertion indices for left and right boundaries
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)
        
        sub = []
        # If left touches or falls inside an existing interval, extend left
        if i % 2 == 0:
            sub.append(left)
        # If right touches or falls inside an existing interval, extend right
        if j % 2 == 0:
            sub.append(right)
            
        self.track[i:j] = sub

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.track, left)
        j = bisect.bisect_left(self.track, right)
        # Check if both endpoints fall within the exact same interval
        return i % 2 == 1 and i == j

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)
        
        sub = []
        # If left falls inside an existing interval, keep the pre-left part
        if i % 2 == 1:
            sub.append(left)
        # If right falls inside an existing interval, keep the post-right part
        if j % 2 == 1:
            sub.append(right)
            
        self.track[i:j] = sub

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)