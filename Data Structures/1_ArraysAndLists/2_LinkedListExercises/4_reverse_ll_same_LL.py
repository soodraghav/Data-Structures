# Helper Code 
#Return Same LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])



def reverse(linked_list):
    """
    Reverse the inputted linked list
    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    prev = None
    current_node = linked_list.head
    
    while current_node != None:
        
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next
        
   # print(prev.value)
    linked_list.head = prev
    
    return linked_list
        
    
        
    

# Tests
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)
#print(llist)

flipped = reverse(llist)
flipped2 = reverse(flipped)
flipped = reverse(flipped2)

print(list(flipped))
   


