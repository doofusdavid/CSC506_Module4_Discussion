from Queue import Queue


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue)

print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
print("Dequeued: ", str(queue.dequeue()))
print(queue)
