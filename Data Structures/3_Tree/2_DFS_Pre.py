# this code makes the tree that we'll traverse

class Node():
    
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        

    def get_value(self):
        return self.value
       
    def set_value(self,value):
        self.value = value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
        
    def has_left_child(self):
        return self.left != None
        
    def has_right_child(self):
        return self.right != None
        
    # define __repr_ to decide what a print statement displays for a Node object
    # def __repr__(self):
    #     return self.get_value()
    
    # def __str__(self):
    #     return self.get_value()
        
class Tree:
    
    def __init__(self, value = None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
        
        
# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_right_child().set_right_child(Node("fruit"))
tree.get_root().get_right_child().set_left_child(Node("goa"))
        
# Let's define a stack to help keep track of the tree nodes
class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"
            
            
class State():
    
    def __init__(self,node):
        self.node =node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def set_visited_left(self):
        self.visited_left = True
        
    def get_visited_left(self):
        return self.visited_left
        
    def get_visited_right(self):
        return self.visited_right
        
    def set_visited_right(self):
        self.visited_right = True
        
    
      


# pre-order traversal using a stack (something's missing)

def pre_order_with_stack(tree):
        
    stack = Stack()
    visit_order = list()
    node = tree.get_root()
    state = State(node)
    stack.push(state)
    # node = stack.top()
    visit_order.append(node.get_value())
    

    while node:

        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
            # node = stack.top()
            
        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)
            # node = stack.top()
            
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
                
            else:
                node =None
                
        
        
    return visit_order
            
    
print(pre_order_with_stack(tree))
    
    
    

