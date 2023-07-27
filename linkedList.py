class Link(object):
    # One datum
    def __init__(self, datum, next=None): #
        self.__data = datum
        # The datum
        self.__next = next
        # Reference
    def getData(self):
    
        # Return the datum stored in this link
        return self.__data
    def setData(self, datum):
        self.__data = datum
        # Change the datum in this Link
    def getNext(self): return self.__next # Return the next link
    def setNext(self, link):
        # Change the next link to a new Link
        if link is None or isinstance(link, Link): #Must be Link or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")
    def isLast(self):
        # Test if link is last in the chain
        return self.getNext() is None # True if & only if no next Link
    def __str__(self):
        # Make a string representation of link
        return str(self.getData())


class LinkedList(object):
    def __init__(self):
        self.__first = None
        # A linked list of data elements
        # Constructor
        # Reference to first Link
    def getFirst(self): return self.__first # Return the first link

    def setFirst(self, link):
        # Change the first link to a new Link
        if link is None or isinstance(link, Link): # It must be None or
            self.__first = link
        # a Link object
        else:
            raise Exception("First link must be Link or None")
    def getNext(self): return self.getFirst()
    # First link is next
    def setNext(self, link): self.setFirst(link) # First link is next
    def isEmpty(self):
        # Test for empty list
        return self.getFirst() is None # True iff no first Link
    def first(self):
        # Return the first item in the list
        if self.isEmpty():
            # as long as it is not empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData() # Return data item (not Link)


    def traverse(self,func=print):
        link = self.getFirst()
        while link is not None:
            func(link.getData())
            link = link.getNext() #
    
    def __len__(self):
        l = 0
        link = self.getFirst()
        while link is not None:
            l += 1
            link = link.getNext()
        return l # Get length of list
    def __str__(self):
        result = "["
        link = self.getFirst()
        while link is not None:
            if len(result) > 1:
                result += " > "
            result += str(link)
            link = link.getNext()
        return result + "]"
    