class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
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
        node_prev = self.head
        while node != None:
            if node.value == val and node == self.head:
                self.head = node.next
                if not all:
                    break
            elif node.value == val and node == self.tail:
                self.tail = node_prev
                node_prev.next = node.next
                if not all:
                    break
            elif node.value == val and node == self.head and node == self.tail:
                self.head = None
                self.tail = None
                if not all:
                    break
            elif node.value == val:
                node_prev.next = node.next
                node = node_prev
                if not all:
                    break
            node_prev = node
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
        if self.head == None:
            self.tail = newNode
            self.head = newNode
            return
        if afterNode == None:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.head
        while node != None:
            node_prev = node
            node = node.next
            if node_prev.value == afterNode.value and node_prev.next == None:
                newNode.next = node
                node_prev.next = newNode
                self.tail = newNode
            if node_prev.value == afterNode.value:
                newNode.next = node
                node_prev.next = newNode









