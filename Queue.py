from Stack import Stack


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        node = self.stack1.pop()
        while node != None:
            self.stack2.push(node)
            node = self.stack1.pop()

        value = self.stack2.pop()

        node = self.stack2.pop()
        while node != None:
            self.stack1.push(node)
            node = self.stack2.pop()
        return value

    def __str__(self):
        return ("Queue Contents: \n" + str(self.stack1))
