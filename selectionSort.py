def selectionSort(self):
    # Sort by selecting min and
    for outer in range(self.__nItems-1): # swapping min to leftmost
        min = outer
        # Assume min is leftmost
        for inner in range(outer+1, self.__nItems): # Hunt to right
            if self.__a[inner] < self.__a[min]: # If we find new min,
                min = inner
                # update the min index
                # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min)
            # Swap leftmost and min