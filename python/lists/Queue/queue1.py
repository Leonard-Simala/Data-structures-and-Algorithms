#implementation using list

# Initializing a queue
queue = []

# Adding elements to the queue ||Enqueueing the queue
queue.append('x')
queue.append('y')
queue.append('z')

print("Initial queue")
print(queue)

# Removing elements from the queue || Dequeueing the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError since the queue is now empty
