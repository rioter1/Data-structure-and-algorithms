class OrderedArray(object):
    def __init__(self, initialSize):
        # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially
    def __len__(self):
        # Special def for len() func
        return self.__nItems
    # Return number of items
    def get(self, n):
        #    Return the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n]
        # only return item if in bounds
        raise IndexError("Index " + str(n) + " is out of range")
    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems):
            # and apply a function
            function(self.__a[j])
    def __str__(self):
        # Special def for str() func
        ans = "["
        # Surround with square brackets
        for i in range(self.__nItems):
            # Loop through items
            if len(ans) > 1:
            # Except next to left bracket,
                ans += ", " # separate items with comma
                ans += str(self.__a[i])
                # Add string form of item
                ans += "]"
        # Close with right bracket
        return ans