# # implementation using collections.dequeue

from collections import deque

# Initializing a queue
q = deque()

# # Adding elements to the queue ||Enqueueing the queue
q.append('x')
q.append('y')
q.append('z')

print("Initial queue")
print(q)

# Removing elements from a queue || Dequeueing the queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError as queue is now empty
