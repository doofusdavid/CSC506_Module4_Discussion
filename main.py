from Queue import Queue


queue = Queue()
print("Enqueue: 1")
queue.enqueue(1)
print("Enqueue: 2")
queue.enqueue(2)
print("Enqueue: 3")
queue.enqueue(3)
print("Enqueue: 4")
queue.enqueue(4)

print(queue)

print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Enqueue: 1000")
queue.enqueue(1000)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
