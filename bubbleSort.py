def bubbleSort(self):
# Sort comparing adjacent vals
    for last in range(self.__nItems-1, 0, -1): # and bubble up
        for inner in range(last):
            # inner loop goes up to last
            if self.__a[inner] > self.__a[inner+1]: # If item less
                self.swap(inner, inner+1) # than adjacent item, swap