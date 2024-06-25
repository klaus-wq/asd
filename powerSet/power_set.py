class PowerSet:

    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)

    def put(self, value):
        if value not in self.store:
            self.store.append(value)

    def get(self, value):
        return value in self.store

    def remove(self, value):
        if value not in self.store:
            return False
        self.store.remove(value)
        return True

    def intersection(self, set2):
        intersection = PowerSet()
        for x in self.store:
            for y in set2.store:
                if x == y:
                    intersection.put(x)
        return intersection

    def union(self, set2):
        union = PowerSet()
        for x in self.store:
            union.put(x)
        for y in set2.store:
            union.put(y)
        return union

    def difference(self, set2):
        difference = PowerSet()
        for x in self.store:
            if x not in set2.store:
                difference.put(x)
        return difference

    def issubset(self, set2):
        if len(self.intersection(set2).store) == set2.size():
            return True
        return False