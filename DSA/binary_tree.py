class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
    def preOrder(self):
        print(self.val,end=' ')
        
        if self.left:
            self.left.preOrder()
            
        if self.right:
            self.right.preOrder()
            
    def inOrder(self):
        if self.left:
            self.left.inOrder()
            
        print(self.val,end=' ')
        
        if self.right:
            self.right.inOrder()
            
    def postOrder(self):
        if self.left:
            self.left.postOrder()
            
        if self.right:
            self.right.postOrder()
            
        print(self.val,end=' ')

root = node(1)

root.left = node(2)
root.right = node(3)

root.left.left = node(4)

print("Pre order Traversal: ", end="")
root.preOrder()
print("\nIn order Traversal: ", end="")
root.inOrder()
print("\nPost order Traversal: ", end="")
root.postOrder()