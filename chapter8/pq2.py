# Q. write a python program to insert new node at the beginning of a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# driver code
ll = LinkedList()

ll.insert_beginning(30)
ll.insert_beginning(20) 
ll.insert_beginning(10)
ll.display()