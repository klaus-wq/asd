class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
        self.step = 3

    def hash_fun(self, key):
        return id(key) % self.size

    def is_key(self, key):
        return key in self.slots

    def get(self, key):
        if self.is_key(key):
            index = self.hash_fun(key)
            self.hits[index] += 1
            return self.values[index]
        return None

    def put(self, key, value):
        index = self.hash_fun(key)
        current_index = index
        while True:
            if self.slots[current_index] == key:
                self.values[index] = value
                return
            if self.slots[index] == None:
                self.slots[index] = key
                self.values[index] = value
                return
            current_index = (current_index + self.step) % self.size
            if current_index == index:
                hits_index = self.hits.index(min(self.hits))
                self.slots[hits_index] = key
                self.values[hits_index] = value
                self.hits[hits_index] = 0
                return




