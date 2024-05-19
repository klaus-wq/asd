from linked_list import *

def sum(list1: LinkedList, list2: LinkedList):
    list = LinkedList()
    if list1.len() == list2.len():
        node1 = list1.head
        node2 = list2.head
        while node1 != None:
            list.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
        list.print_all_nodes()
        return list







