class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_node(self):
        print(self.data)

root = Node(10)
root.print_node()