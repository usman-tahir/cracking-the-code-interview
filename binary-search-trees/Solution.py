from Node import *
from random import *

def check_binary_search_tree(root):
    elements = print_in_order(root)

    for e in range(1, len(elements)):
        if not elements[e] > elements[e - 1]:
            return False
    return True

root = Node(0)
for x in range(1, 10):
    root.insert(root, x)
print(check_binary_search_tree(root))
