
#Implement a queue using an array
"""
After putting in element in arr[]
"""

class Queue():
    def __init__(self, queue_size: int= 10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0
        
    # TODO: Add the enqueue method
    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0
 
    #3. Add the size, is_empty, and front methods           
    def size(self):
        return self.queue_size
        
    def is_empty(self):
        return self.queue_size == 0
        
    def front(self):
        if self.front_index ==-1:
            return None
        else:
            return self.arr[self.front_index]
            
            
    #4. Add the dequeue method

    def dequeue(self):
        
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None
        
        value = self.arr[self.front_index]
        self.queue_size -=1
        self.front_index = (self.front_index +1) % len(self.arr)
        return value
        
    # TODO: Add the _handle_queue_capacity_full method
    def _handle_queue_capacity_full(self):
        
        if self.queue_size == len(self.arr):
            temp = self.arr
            self.arr = [0 for _ in range(2*len(arr))]
            
        index = 0
        
        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index,len(self.arr)):
            self.arr[index] = temp[i]
            index +=1
        
        # case: when front-index is ahead of next index    
        for i in range(0,self.front_index):
            self.arr[index] = temp[i]
            index +=1
            
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
            
        

            
            
        