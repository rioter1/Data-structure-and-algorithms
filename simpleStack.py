class Stack(object):
    def __init__(self, max):
        self.__stackList = [None] * max
        self.__top = -1
        # Constructor
        # The stack stored as a list
        # No items initially
    def push(self, item):
        # Insert item at top of stack
        self.__top += 1
        # Advance the pointer
        self.__stackList[self.__top] = item # Store item
    def pop(self):
        # Remove top item from stack
        top = self.__stackList[self.__top]
        # Top item
        self.__stackList[self.__top] = None # Remove item reference
        self.__top -= 1
        # Decrease the pointer
        return top
        # Return top item
    def peek(self):
        # Return top item
        if not self.isEmpty():
        # If stack is not empty
            return self.__stackList[self.__top] # Return the top item
    def isEmpty(self):
        return self.__top < 0
        # Check if stack is empty
    def isFull(self):
        # Check if stack is full
        return self.__top >= len(self.__stackList) - 1
    def __len__(self):
        return self.__top + 1
    # Return # of items on stack
    def __str__(self):
        #
        ans = "["
        #
        for i in range(self.__top + 1): #
            if len(ans) > 1:
                #
                ans += ", "
                #
            ans += str(self.__stackList[i])
    
        # Add string form of itemans += "]"
        return ans