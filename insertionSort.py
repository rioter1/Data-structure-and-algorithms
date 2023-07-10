def insertionSort(self):
    # Sort by repeated inserts
    for outer in range(1, self.__nItems): # Mark one element
        temp = self.__a[outer]
        # Store marked elem in temp
        inner = outer
        # Inner loop starts at mark
        while inner > 0 and temp < self.__a[inner-1]: # If marked
            self.__a[inner] = self.__a[inner-1] # elem smaller, then
            inner -= 1
            # shift elem to right
        self.__a[inner] = temp
        # Move marked elem to ’hole’