class Queue:
    
    def __init__(self):
        self.queue = []
        self.count = 0

    def enqueue(self, data):
        self.queue.insert(0, data)
        self.count += 1

    def dequeue(self):
        self.count -= 1
        return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]

    def empty(self):
        return self.count == 0

    def size(self):
        return self.count

q = Queue()

q.enqueue("dog")
q.enqueue("cat")
q.enqueue("rabbit")

print(q.size())
print(q.peek())
print(q.empty())