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
        string = "Stack 1: \n"
        string = string + str(self.stack1)
        string = string + "Stack 2:"
        string = string + str(self.stack2)
        return string
