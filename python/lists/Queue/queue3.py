#  implementation of using queue module


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize of the Queue
print(q.qsize())

# Adding of element to queue
q.put('x')
q.put('y')
q.put('z')

# Return Boolean for Full Queue
print("\n Queue is Full: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty Queue
print("\nQueue is Empty: ", q.empty())

q.put(1)
print("\n Queue is Empty: ", q.empty())
print("Queue is Full: ", q.full())

# This would result into InfiniteLoop as the Queue is empty.
# print(q.get())
