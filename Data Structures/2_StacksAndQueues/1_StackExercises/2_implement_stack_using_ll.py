#Node Class

# Add the Node class here
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

"""
In the cell below, see if you can write the __init__ method for our Stack class. It will need two attributes:
A head attribute to keep track of the first node in the linked list
A num_elements attribute to keep track of how many items are in the stack
"""

class Stack:
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
   
        

#3. Add the push method
#Next, we need to define our push method, so that we have a way of adding elements to the top of the stack.


    def push(self,value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.num_elements +=1
        
        
#Size and is empty

    def size(self):
        return self.num_elements
       
        
    def is_empty(self):
        return self.num_elements == 0
        
        
        

#Add the pop method

#The method needs to:

#Check if the stack is empty and, if it is, return None
#Get the value from the head node and put it in a local variable
#Move the head so that it refers to the next item in the list
#Return the value we got earlier"""


    def pop(self):
        if self.is_empty():
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
        
    
# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")
