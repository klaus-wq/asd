class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
         return id(key) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        if self.is_key(key):
            self.values[index] = value
        else:
            self.slots[index] = key
            self.values[index] = value

    def get(self, key):
        if self.is_key(key):
            index = self.hash_fun(key)
            return self.values[index]
        return None




