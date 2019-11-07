# Tree traversal

class Node():
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

#Inorder traversal

def inorder(root):
    if root:
        inorder(root.left)

        print(root.val)

        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)

        preorder(root.left)

        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)

        postorder(root.right)

        print(root.val)


##driver function
#adding node values

root = Node(1)
root.left = Node(5)
root.right = Node(8)
root.left.left = Node(5)
root.right.right = Node(7)
root.left.left.left = Node(4)

postorder(root)
