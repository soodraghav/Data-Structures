class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class SinglyLinkedList:
    """
    In singly linked list, each node in the list is connected only to the
    next node in the list.
    """
    def __init__(self):
        self.tail = None
        self.head = None
        
    def append_no_tail(self, val):
        """
        Appends a new-node to the tail node.
        This append operation will take an order O(n) as it has to loop
        through each element in a list to find the last (tail) node and
        insert at the right-most end.
        """
        
        if self.head == None:
            self.head = Node(val)
            
        else:
            
            current_node = self.head
            
            while current_node.next != None:
                current_node = current_node.next
                
            current_node.next = Node(val)
            
            return self.head
            
            
    
    def append_with_tail(self, val):
        """
        Append a new node to tail node:
        This operation will take an order of O(1) in time-complexity but it
        will take an extra pointer for each node. Therefore the space
        complexity is increased. Ofter times, it is a trade off between the 2.
        """

        if self.head == None:
            self.head = Node(val)
            self.tail =  self.head
            
            
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            
        return self.head
        
    
    def to_list(self):
        """
        Converts a linked list back into a Python list.
        """
        values = []
        current_node = self.head

        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next

        return values    



# Test cases
print('Append at end without using tail:')
linked_list = SinglyLinkedList()
linked_list.append_no_tail(1)
linked_list.append_no_tail(2)
linked_list.append_no_tail(4)

node = linked_list.head
while node:
    print(node.val)
    node = node.next

print('Append to end using tail:')
linked_list = SinglyLinkedList()
linked_list.append_with_tail(1)
linked_list.append_with_tail(2)
linked_list.append_with_tail(4)

node = linked_list.head
while node:
    print(node.val)
    node = node.next

print('To list test:')
linked_list = SinglyLinkedList()
linked_list.append_no_tail(3)
linked_list.append_no_tail(2)
linked_list.append_no_tail(-1)
linked_list.append_no_tail(0.2)

print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")