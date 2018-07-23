class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def children_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count +=1
        return count

    def insert(self, data):
        if self.data: # parent
            if data < self.data: # if new data is less than parent -> left hand side
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data: # if new data is more than parent -> right hand side
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        #get node
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()  #TODO: write this method.
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    self.data = None
            elif children_count == 1:
                #if node has 1 child, replace node with its child.
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children, find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                    #replace node data by its successor data
                    node.data = successor.data
                    #fix successor's parent's child
                    if parent.left == successor:
                        parent.left = successor.right
                    else:
                        parent.right = successor.right

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

node, parent = root.lookup(3)
print(node.data, parent.data)

root.print_tree()
root.delete(12)
print("--------------------")
root.print_tree()