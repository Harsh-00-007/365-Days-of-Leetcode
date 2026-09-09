class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k               # Maximum capacity
        self.q = [0] * k         # Fixed-size array to store the elements
        self.head = 0            # Pointer to the front element
        self.size = 0            # Current number of elements in the deque

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move head backwards circularly
        self.head = (self.head - 1) % self.k
        self.q[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        # Find the next available spot at the tail circularly
        tail = (self.head + self.size) % self.k
        self.q[tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Move head forwards circularly
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Simply reduce the size; the rear element is effectively dropped
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        # Calculate the index of the actual last element circularly
        tail = (self.head + self.size - 1) % self.k
        return self.q[tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k