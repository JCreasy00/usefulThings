# Recursive algorithm for inorder binary tree traversal

# node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inOrderTraversalR(root: Node, result) -> None:
    
    if root: # if root exists
        inOrderTraversalR(root.left, result) # traverse left
        result.append(root.val) # append to result
        inOrderTraversalR(root.right, result) # traverse right after every append
    return result # return result at the end
    

# example traversal
result = []
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(inOrderTraversalR(root, result))

