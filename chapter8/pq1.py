# Q. write a python program to create a singly linked list and display its elements.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes
first = Node(10)
second = Node(20)
third = Node(30)

# link the nodes
first.next = second
second.next = third

# display the elements
current = first
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")