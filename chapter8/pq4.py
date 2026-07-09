# Q. write a python program to delete a node from a singly linked list by its value.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list class
class LinkedList:
    def __init__(self):
        self.head = None

#insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    #delete a node by value
    def delete_by_value(self, value):
        if self.head is None:
            return
        
        # If the node to be deleted is the head
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head

        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    #display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#driver code
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.display()

print ("Before deletion:")
ll.display()

ll.delete_by_value(20)
print("After deletion:")
ll.display()