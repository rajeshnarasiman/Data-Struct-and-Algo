# constructing root
class Node:
    def __init__(self, k):
        self.root = k
        self.left = None
        self.right = None
        
#Sorting the binary search tree
def sortingBST(arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = sortingBST(arr[:mid])
    root.right = sortingBST(arr[mid+1:])
    return root

#Finding least common Ancestor
class Node: 
      
    # Constructor to create a new tree node 
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
        
def least_ancestor(root, n1, n2):
    if not root:
        return None
    if root.key == n1 or root.key == n2:
        return root
    left_item = least_ancestor(root.left, n1, n2)
    right_item = least_ancestor(root.right, n1, n2)
    if left_item and right_item:
        return root
    return left_item if left_item is not None else right_item

#Driver function
arr = [1,2,4,66,77,88,99]
root = sortingBST(arr)
print("Least common ancestor of (2,77) is:")
least_ancestor(root, 2, 77).key
