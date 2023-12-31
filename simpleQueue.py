class Queue(object):
    def __init__(self, size):
        self.__maxSize = size
        self.__que = [None] * size
        self.__front = 1
        self.__rear = 0
        self.__nItems = 0
        
    
    def insert(self, item):
        # Insert item at rear of queue
        if self.isFull():
        # if not full
            raise Exception("Queue overflow")
        self.__rear += 1
        # Rear moves one to the right
        if self.__rear == self.__maxSize: # Wrap around circular array
            self.__rear = 0
        self.__que[self.__rear] = item # Store item at rear
        self.__nItems += 1
        return True
    def remove(self):
        #    Remove front item of queue
        if self.isEmpty():
        # and return it, if not empty
            raise Exception("Queue underflow")
        front = self.__que[self.__front] # get the value at front
        self.__que[self.__front] = None # Remove item reference
        self.__front += 1
        # front moves one to the right
        if self.__front == self.__maxSize: # Wrap around circular arr.
            self.__front = 0
        self.__nItems -= 1
        return front
    def peek(self):
        # Return frontmost item
        return None if self.isEmpty() else self.__que[self.__front]
    def isEmpty(self): return self.__nItems == 0
    def isFull(self): return self.__nItems == self.__maxSize
    def __len__(self): return self.__nItems
    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:
                j -= self.__maxSize
            ans += str(self.__que[j])
        ans += "]"
        return ans
    '''We set __front to 1 initially, as shown in the empty queue, so that when the first element is inserted and __rear is incremented, they both
are 1. Thats desirable because the first and last items in the queue are one and the same. So
__rear and __front are 1 for the first item, and __rear is increased for the insertions that
follow. That means the frontmost items in the queue are at lower indices, and the rearmost are
at higher indices, in general.'''