# Helper Code 
#Return Different LinkedList


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
    new_linked_list = LinkedList()
    current_node = linked_list.head
    
    while current_node != None:
        
        
        if new_linked_list.head == None:
            new_linked_list.head = Node(current_node.value)
        
        else:    
            new_node = Node(current_node.value)
            new_node.next = new_linked_list.head
            new_linked_list.head = new_node
        
        current_node = current_node.next
        
   
    
    return new_linked_list
        
    
        
    

# Tests
llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
