# python3
class Node:
    # signifies binary tree here.
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
def printLevelOrder(root):
    h = height(root)
    for level in range(1, h+1):
        printGivenLevel(root, level)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end = " ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# Driver program to test above function
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)