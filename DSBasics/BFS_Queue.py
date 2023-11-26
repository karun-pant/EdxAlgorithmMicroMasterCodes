# python3

class Node:
    # signifies binary tree here.
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        
def printLevelOrder(root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.data, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(54)
    root.right.right = Node(75)
 
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)