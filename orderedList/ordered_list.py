class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return - 1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        node = self.head
        while node != None:
            if (self.__ascending and self.compare(value, self.head.value) <= 0) or (not self.__ascending and self.compare(value, self.head.value) >= 0):
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
                break
            if (self.__ascending and self.compare(value, self.tail.value) >= 0) or (not self.__ascending and self.compare(value, self.tail.value) <= 0):
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
                break
            if (self.__ascending and self.compare(value, node.value) <= 0) or (not self.__ascending and self.compare(value, node.value) >= 0):
                new_node.prev = node.prev
                new_node.next = node
                if node.prev is not None:
                    node.prev.next = new_node
                node.prev = new_node
                break
            node = node.next


    def find(self, val):
        node = self.head
        while node != None:
            if (self.__ascending and node.value > val) or (not self.__ascending and node.value < val):
                return None
            if self.compare(node.value, val) == 0:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if self.len() == 1:
            self.head = None
            self.tail = None
            return
        if node:
            if node == self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            if node == self.tail:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                return
            node.next.prev = node.prev
            node.prev.next = node.next
            return

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def get_all_values(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super().compare(v1.strip(), v2.strip())