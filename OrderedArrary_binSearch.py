class OrderedArray(object):

    def find(self, item):
        # Find index at or just below
        lo = 0
        # item in ordered list
        hi = self.__nItems-1
        # Look between lo and hi
        while lo <= hi:
            mid = (lo + hi) // 2
            # Select the midpoint
            if self.__a[mid] == item: # Did we find it at midpoint?
                return mid
            # Return location of item
            elif self.__a[mid] < item: # Is item in upper half?
                lo = mid + 1
            # Yes, raise the lo boundary
            else:
                hi = mid - 1
            # No, but could be in lower half
        return lo
            # Item not found, return insertion point instead

    def search(self, item):
        index = self.find(item)
        # Search for item
        if index < self.__nItems and self.__a[index] == item:
            return self.__a[index]
        # and return item if found
    def insert(self, item): # Insert item into correct position
        if self.__nItems >= len(self.__a): # If array is full,
            raise Exception("Array overflow") # raise exception
        index = self.find(item)
        # Find index where item should go
        for j in range(self.__nItems, index, -1): # Move bigger items
            self.__a[j] = self.__a[j-1]
            # to the right
            self.__a[index] = item
            # Insert the item
        self.__nItems += 1
        # Increment the number of items
    def delete(self, item):
        # Delete any occurrence
        j = self.find(item)
        # Try to find the item
        if j < self.__nItems and self.__a[j] == item: # If found,
            self.__nItems -= 1
        # One fewer at end
        for k in range(j, self.__nItems): # Move bigger items left
            self.__a[k] = self.__a[k+1]
            return True
        # Return success flag
        return False
        # Made it here; item not found