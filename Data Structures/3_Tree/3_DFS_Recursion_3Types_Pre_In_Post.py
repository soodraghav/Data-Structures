#DFS using Recursion

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

        
class Tree:
    
    def __init__(self, value = None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
        
        
# create a tree and add some nodes
tree = Tree("a")
tree.get_root().set_left_child(Node("b"))
tree.get_root().set_right_child(Node("e"))
tree.get_root().get_right_child().set_right_child(Node("f"))
tree.get_root().get_left_child().set_left_child(Node("c"))
tree.get_root().get_left_child().set_right_child(Node("d"))


#Pre Order DFS using Recursion
def pre_order(tree):
    
    visit_order = list()
    node = tree.get_root()
   
    def visit(node):
        if node:
           visit_order.append(node.get_value())
        
        if node.has_left_child():
            visit(node.get_left_child())

            
        if node.has_right_child():
            visit(node.get_right_child())
          
    visit(node)
    
    return visit_order

print(pre_order(tree))


#In Order DFS using Recursion
def in_order(tree):
    
    visit_order = []
    
    def visit1(node):
        
        if node.has_left_child():
            visit1(node.get_left_child())
            
        if node:    
            visit_order.append(node.get_value())
            
        if node.has_right_child():
            visit1(node.get_right_child())
            
    visit1(tree.get_root())
    
    return visit_order
    
print(in_order(tree))

#Post Order DFS using Recursion
def post_order(tree):
    
    visit_order = []
    
    def visit(node):
        
        if node.has_left_child():
            visit(node.get_left_child())
        
        if node.has_right_child():
            visit(node.get_right_child())
            
        if node:
            visit_order.append(node.get_value())
            
    visit(tree.get_root())
    
    return visit_order
    
print(post_order(tree))
            
        
            
        

    

