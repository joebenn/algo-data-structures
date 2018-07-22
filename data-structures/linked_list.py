class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    #Print linked list
    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    #Add new node at begining of linked list.
    def addBegining(self, newData):
        newNode = Node(newData)
        #Update the new nodes next val to existing node
        newNode.nextval = self.headval
        self.headval = newNode

    #Add new node at the end of the linked list
    def addEnd(self, newData):
        newNode = Node(newData)
        if self.headval is None:
            self.headval = newNode
            return
        lastNode = self.headval
        while(lastNode.nextval):
            lastNode = lastNode.nextval
        lastNode.nextval = newNode

    #Add new node at position after 'preNode'
    def addBetween(self, preNode, newData):
        if preNode is None:
            print("Node supplied is absent")
            return
        newNode = Node(newData)
        newNode.nextval = preNode.nextval
        preNode.nextval = newNode
    

list1 = SLinkedList()
list1.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

list1.headval.nextval = e2
e2.nextval = e3

list1.print_list()

print("------")

list1.addBetween(list1.headval, "Friday")

list1.print_list()
