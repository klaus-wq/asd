class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0


    def hash1(self, str1):
        res = 0
        for c in str1:
            res = res * 17 + ord(c)
        return res % self.filter_len

    def hash2(self, str1):
        res = 0
        for c in str1:
            res = res * 223 + ord(c)
        return res % self.filter_len

    def add(self, str1):
        self.filter = self.filter | self.hash1(str1)
        self.filter = self.filter | self.hash2(str1)

    def is_value(self, str1):
        return self.filter & self.hash1(str1) > 0 and self.filter & self.hash2(str1) > 0