class Node():
    
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
        

    def get_value(self):
        return self.value()
       
    def set_value(self,value):
        self.value = value
        
    def set_left_child(self,node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
    
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
        
        
node0 = Node("apple")
node1 = Node("BANANA")
node2 = Node("Bluecheese")


# node0.set_left_child(node1)
node0.set_right_child(node2)

print(node0.value)
# print(node0.left.value)
print(node0.has_left_child())


