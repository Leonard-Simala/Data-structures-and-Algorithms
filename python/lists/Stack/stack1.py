# implemetntation of a stack as ana array

#Returns -infinite when stack is empty
from sys import maxsize

def createStack():
    # a stack of plates for example
    stack = []
    return stack
# stack is empty when size ==0
def isEmpty(stack):
    return len(stack) == 0

# Adding an item to stack. increases size by 1
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

# Removing an item from stack. decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite
     
    return stack.pop()
    
# Function to return the top from stack without removing it
def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite
    return stack[len(stack) - 1]
 
# Driver program to test above functions   
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")