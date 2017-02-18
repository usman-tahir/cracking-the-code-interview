
class Node:
    def __init__(self, data):
        self.size = 1
        self.data = data
        self.left = None
        self.right = None

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def insert(self, root, data):
        if root == None:
            root = Node(data)
            return

        if data < root.data:
            if root.left != None:
                self.insert(root.left, data)
            else:
                root.left = Node(data)
                self.size += 1
        else:
            if root.right != None:
                self.insert(root.right, data)
            else:
                root.right = Node(data)
                self.size += 1

# Printing the BST in order
def print_in_order(root, result = []):
    result = result
    if not root:
        return
    print_in_order(root.left, result)
    # print(root.data)
    result.append(root.data)
    print_in_order(root.right, result)
    return result

def print_pre_order(root, result = []):
    result = result
    if not root:
        return
    # print(root.data)
    result.append(root.data)
    print_pre_order(root.left, result)
    print_pre_order(root.right, result)
    return result

def print_post_order(root, result = []):
    result = result
    if not root:
        return
    print_post_order(root.left, result)
    print_post_order(root.right, result)
    # print(root.data)
    result.append(root.data)
