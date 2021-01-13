"""
Linked List Practice
Implement a linked list class. Your class should be able to:
- Append data to the tail of the list and prepend to the head
- Search the linked list for a value and return the node
- Remove a node
- Pop, which means to return the first node's value and delete the node from
the list
- Insert data at some position in the list
- Return the size (length) of the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list - O(1)"""
        
        if self.head == None:
            self.head = Node(value)
            
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        

    def append(self, value):
        """ Append a value to the end of the list - O(n)"""
        
        if self.head == None:
            self.head = Node(value)
            
        else:
            
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
                
            current_node.next = Node(value)
            
        

        

    def search(self, value):
        """
        Search the linked list for a node with the requested value and return
        the node - O(n)
        """
        if self.head == None:
            return None
            
        else:
            current_node = self.head
            
            while current_node != None:
                
                if current_node.value == value:
                    return current_node
                    
                else:
                    current_node = current_node.next
                    
            return None
        

    def remove(self, value):
        """ Delete the first node with the desired data. """
        if self.head == None:
            return None
        
        elif self.head.value == value:
            temp = self.head
            self.head = self.head.next
            
            return temp
            
        else:
            current_node = self.head
            
            while current_node != None:
                
                if current_node.next.value == self.value:
                    temp = current_node.next
                    current_node.next = current_node.next.next
                    return temp
                
                else:
                    current_node = current_node.next
                    
        return None
                    
                    
                    
        

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None

        else:
            pop_item = self.head.value
            self.head = self.head.next
            return pop_item
        

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return 
        
        index = 0
        current_node = self.head
        
        while pos > index:
            current_node = current_node.next
            index +=1
            
            if pos-1 == index:
                join = current_node.next
                new_node = Node(value)
                current_node.next = new_node
                new_node.next = join
                
                return None
                
        self.append(value)
            
            
        

    def size(self):
        size = 0
        
        self.head = current_node
        
        while current_node:
            size += 1
            current_node = current_node.next
            
        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out
        

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
        


# Test prepend
print('Prepend test:')
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test append
print('Append test:')
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test search
print('Search test:')
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
print('Search values: %s, %s' %
      (linked_list.search(1).value, linked_list.search(4).value))
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test remove
print('Remove test:')
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test pop
print('Pop test:')
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test insert
print('Insert test:')
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.print_list()
print('*' * 10)

# Test size
print('Size test:')
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
print(linked_list.size())
print('*' * 10)