class Set:

    # Creates an empty set instance.
    def __init__(self, initialCount):
        self._s = []

        i = 0
        while i < initialCount:
            e = int(input("Enter element to be added: "))
            if e not in self._s:
                self.add(e)
                i += 1
            else:
                print(e, " already present in set")

    def __str__(self):
        string = "{"
        for i in range(len(self.get_set())):
            string = string + str(self.get_set()[i])
            if i != len(self.get_set()) - 1:
                string = string + ", "
        string = string + "}"
        return string

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._s)

    # Determines if an element is in the set.
    def __contains__(self, e):
        return e in self._s

    def get_set(self):
        return self._s

    # Determines if the set is empty.
    def isEmpty(self):
        return len(self._s) == 0

    # Adds a new unique element to the set.
    def add(self, e):
        if e not in self:
            self._s.append(e)

    # Removes an e from the set.
    def remove(self, e):
        if e in self.get_set():
            self.get_set().remove(e)

    # Determines if this set is a subset of setB
    def isSubsetOf(self, setB):
        for e in setB.get_set():
            if e not in self.get_set():
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = self
        for e in setB:
            if e not in self.get_set():
                newSet.add(e)
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def intersection(self, setB):
        newSet = Set(0)
        for i in range(len(self.get_set())):
            for j in range(len(setB.get_set())):
                if self.get_set()[i] == setB.get_set()[j]:
                    newSet.add(self.get_set()[i])
        return newSet

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        newSet = Set(0)
        for e in self.get_set():
            if e not in setB.get_set():
                newSet.add(e)
        return newSet

    # Creates the iterator for traversing the list of items
    def __iter__(self):
        return iter(self._s)

