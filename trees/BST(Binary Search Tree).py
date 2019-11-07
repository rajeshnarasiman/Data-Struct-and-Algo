class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
        
#Getting the structure of tree        
def sortingarray(arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = sortingarray(arr[:mid])
    root.right = sortingarray(arr[mid+1:])
    return root

# To get the pre order sorting:
def preorder(node):
    if not node:
        return 
    print(node.data)
    preorder(node.left)
    preorder(node.right)


# To get the BST (Post order sorting):
def post_order(node):
    if not node:
        return 
    post_order(node.left)
    post_order(node.right)
    print(node.data)

# To get the pre order sorting:
def Inorder(node):
    if not node:
        return
    Inorder(node.left)
    print(node.data)
    Inorder(node.right)
    

#Driver function:
arr = [1,3,4,5,6,7,9]
root = sortingarray(arr)
print("Inorder BST is :")
Inorder(root)
print("Post order BST is :")
post_order(root)
print("Pre order BST is :")
preorder(root)
