class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return id(value) % self.size

    def seek_slot(self, value):
        index = self.hash_fun(value)
        current_index = index
        while True:
            if self.slots[current_index] == None:
                return current_index
            current_index = (current_index + self.step) % self.size
            if current_index == index:
                return None


    def put(self, value):
        index = self.seek_slot(value)
        if index != None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        index = self.hash_fun(value)
        current_index = index
        while True:
            if self.slots[current_index] == value:
                return current_index
            if self.slots[index] == None:
                return None
            current_index = (current_index + self.step) % self.size
            if current_index == index:
                return None

    def print_hash_table(self):
        res = []
        for i in self.slots:
            res.append(i)
        return res





