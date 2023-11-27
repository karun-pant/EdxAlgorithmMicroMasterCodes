# python3

class Node:
    # signifies binary tree here.
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
# Function to perform in-order traversal of a binary tree.
# It recursively visits the left subtree, then prints the data of the current node, 
# and finally visits the right subtree.
def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)
    
# This code snippet implements the pre-order traversal of a binary tree.
# It recursively visits the root node, then visits the left subtree,
# and finally visits the right subtree.
def preOrder(root):
    if root is None:
        return 
    print(root.data, end = " ")
    preOrder(root.left)
    preOrder(root.right)
    
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end = " ")
    
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(54)
    root.right.right = Node(75)
 
    print("In-order traversal of binary tree is -")
    inOrder(root)
    print("Pre-order traversal of binary tree is -")
    preOrder(root)
    print("Post-order traversal of binary tree is -")
    postOrder(root)