class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

# Link first Node to second Node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3