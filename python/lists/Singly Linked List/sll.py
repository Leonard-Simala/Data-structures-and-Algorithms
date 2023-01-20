# structure of Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.last_node = None

	# function to add elements to linked list
	def append(self, data):
		# if linked list is empty then last_node will be none so in if condition head will be created
		if self.last_node is None:
			self.head = Node(data)
			self.last_node = self.head
		# adding node to the tail of linked list
		else:
			self.last_node.next = Node(data)
			self.last_node = self.last_node.next

# function to print the content of linked list
	def display(self):
		current = self.head
	# traversing the linked list
		while current is not None:
		# at each node printing its data
			print(current.data, end=' ')
		# giving current next node
			current = current.next
		print()

# Driver code
if __name__ == '__main__':
	L = LinkedList()
	# adding elements to the linked list
	L.append(21)
	L.append(44)
	L.append(77)
	# displaying elements of linked list
	L.display()
