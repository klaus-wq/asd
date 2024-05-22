class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        res_nodes = []
        while node != None:
            res_nodes.append(node.value)
            node = node.next
        return res_nodes

    def find(self, val):
        node = self.head
        while node != None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node != None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head
        while node != None:
            if node.value == val and node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                if not all:
                    break
            elif node.value == val and node == self.head:
                self.head = node.next
                node.next.prev = node.prev
                if not all:
                    break
            elif node.value == val and node == self.tail:
                self.tail = node.prev
                node.prev.next = node.next
                if not all:
                    break
            elif node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    break
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        total_length = 0
        node = self.head
        while node != None:
            total_length += 1
            node = node.next
        return total_length

    def insert(self, afterNode, newNode):
        if afterNode == None:
            if self.head == None:
                self.add_in_head(newNode)
            else:
                self.add_in_tail(newNode)
        else:
            node = self.head
            while node != None:
                if node.value == afterNode.value:
                    newNode.next = node.next
                    newNode.prev = node
                    if node.next == None:
                        self.tail = newNode
                    if node.next != None:
                        node.next.prev = newNode
                    node.next = newNode
                    break
                node = node.next

    def add_in_head(self, newNode):
        if self.head == None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode






