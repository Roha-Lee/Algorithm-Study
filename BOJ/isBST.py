from tabnanny import check


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left 
        self.right = right 
        self.value = value

def is_binary_search_tree(node, min_value, max_value):
    if node is None:
        return True

    if min_value < node.value < max_value:
        return is_binary_search_tree(node.left, min_value, node.value) and is_binary_search_tree(node.right, node.value, max_value)
    else:
        return False

left = Node(3, Node(1), Node(4))
right = Node(7, Node(6), Node(8))
root = Node(5, left, right)
print(is_binary_search_tree(root, -float('inf'), float('inf')))