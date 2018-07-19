class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    def addBegining(self, newData):
        NewNode = Node(newData)
        #Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

list1 = SLinkedList()
list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

list1.headval.nextval = e2
e2.nextval = e3

list1.print_list()

list1.addBegining("Sunday")
print("-----")

list1.print_list()