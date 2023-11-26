# python3

import sys
import threading

class Node:
    def __init__(self, data):
        self.isRoot = False
        self.data = data
        self.children = None

    def addChild(self, child):
        if self.children is None:
            self.children = [child]
        else:
            self.children.append(child)

def compute_height(tree):
    if tree.children == None:
        return 0
    height = 1 + max(compute_height(child) for child in tree.children)
    return height

def makeTree(n, parents):
    nodes = []
    root = None
    for item in parents:
        nodes.append(Node(item))

    for i in range(n):
        if parents[i] == -1:
            nodes[i].isRoot = True
            root = nodes[i]
        else:
            nodes[parents[i]].addChild(nodes[i])
    return root

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = makeTree(n, parents)
    height = 1 + compute_height(tree) # 1 is added for root 
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
