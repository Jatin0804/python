class node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
        
def inOrder(root):
    
    if root:
        inOrder(root.left)
        print(str(root.val)+" -> ",end=' ')
        inOrder(root.right)
        
def postOrder(root):
    
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.val)+" -> ",end=' ')
        
def preOrder(root):
    
    if root:
        print(str(root.val)+" -> ",end=' ')
        preOrder(root.left)
        preOrder(root.right)
        
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
root.left.left.left=node(8)
root.left.right.right=node(9)

print("Inorder traversal : ")
inOrder(root)
print("\nPreOrder traversal : ")
preOrder(root)
print("\nPostOrder traversal")
postOrder(root)