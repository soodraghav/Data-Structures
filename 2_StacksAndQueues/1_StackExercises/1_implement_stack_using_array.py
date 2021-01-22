"""
In the cell below:

Define a class named Stack and add the __init__ method
Initialize the arr attribute with an array containing 10 elements, like this: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Initialize the next_index attribute
Initialize the num_elements attribute
"""


class Stack:
    
    def __init__(self,initial_size =10):
        self.arr = [0 for i in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    #Push Method
    
    def push(self, element):
        
        
        #To handle full capacity
        
        if len(self.arr) == self.next_index:
            print("Out of space! Increasing capacity!!")
            self.handle_stack_capacity()
        
        self.arr[self.next_index] = element
        self.next_index +=1
        self.num_elements +=1
        
        
    def handle_stack_capacity(self):
        old_arr = self.arr
        
        self.arr = [0 for i in range(2*len(old_arr))]
        
        for index,value in enumerate(old_arr):
            self.arr[index] = value
            
    
    def pop(self):
        
        if self.is_empty():
            self.next_index = 0
            return None
        
        self.next_index -=1
        self.num_elements -=1
        
        return self.arr[self.next_index]
        
        
    def is_empty(self):
        return self.num_elements == 0
        
        
    def size(self):
        return self.num_elements
        
        
        
    
    

foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # The array is now at capacity!
foo.push(11) # This one should cause the array to increase in size
print(foo.arr) # Let's see what the array looks like now!
print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.
    
        
        


