class Node:
    
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
class Queue:
    
# 2. Create the Queue class and its __init__ method
# In the cell below, see if you can write the __init__ method for our Queue class. It will need three attributes:

# A head attribute to keep track of the first node in the linked list
# A tail attribute to keep track of the last node in the linked list
# A num_elements attribute to keep track of how many items are in the stack    
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        

# 3. Add the enqueue method
# In the cell below, see if you can figure out how to write the enqueue method.

# Remember, the purpose of this method is to add a new item to the back of the queue. Since we're using a linked list, this is equivalent to creating a new node and adding it to the tail of the list.

# Some things to keep in mind:

# If the queue is empty, then both the head and tail should refer to the new node (because when there's only one node, this node is both the head and the tail)
# Otherwise (if the queue has items), add the new node to the tail (i.e., to the end of the queue)
# Be sure to shift the tail reference so that it refers to the new node (because it is the new tail)
    
    def enqueue(self,val):
        
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
            self.num_elements +=1
            current_node = self.tail

        
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.num_elements +=1
        
        
            
# 4. Add the size and is_empty methods
# You've implemented these a couple of times now, and they'll work the same way here:

# Add a size method that returns the current size of the stack
# Add an is_empty method that returns True if the stack is empty and False otherwise
# We'll make use of these methods in a moment when we write the dequeue method.

    def size(self):
        return self.num_elements
        
        
    def is_empty(self):
        return self.size() == 0
        
        
# 5. Add the dequeue method
# In the cell below, see if you can add the deqeueue method.

# Here's what it should do:

# If the queue is empty, it should simply return None. Otherwise...
# Get the value from the front of the queue (i.e., the head of the linked list)
# Shift the head over so that it refers to the next node
# Update the num_elements attribute
# Return the value that was dequeued        
            
            
    def dequeue(self):
        
        if self.is_empty():
            return None
        
        else:
            value = self.head.val
            self.head = self.head.next
            self.num_elements -= 1
            
            return value
        

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
        
        
        
        
        