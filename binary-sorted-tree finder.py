'''
Given a tree, find the largest tree/subtree that is a BST (binary sorted tree).

Given a tree, return the size of the largest tree/subtree that is a BST.
'''

# a useful module for generating trees
from binarytree import tree 


class data:
    def __init__(self, BSTroot, state, node_count, min, max):
        self.BSTroot = BSTroot
        self.state = state
        self.node_count = node_count
        self.min = min
        self.max = max

def BST_check(node):
    # Used in case left or right node is not present
    if not node:
        return None

    if node.left == None and node.right == None:
        node_data = data(node, True, 1, node.value, node.value)
        return node_data


    left = BST_check(node.left)

    right = BST_check(node.right)

    # If there is only one child node
    # Checks if minimum of right node is greater than the node
    if left == None and right != None:
        if (right.state == True) and (node.value < right.min):
            node_data = data(node, True, right.node_count + 1, node.value, right.max)
        else:
            node_data = data(right.BSTroot, False, right.node_count, None, None)

    # Checks if maximum of left node is smaller than the node
    elif left != None and right == None :
        if (left.state == True) and (node.value >= left.max):
            node_data = data(node, True, left.node_count + 1, left.min, node.value)
        else:
            node_data = data(left.BSTroot, False, left.node_count, None, None)

    # If there are two child nodes
    # Checks if node value is greater than maximum of left node and smaller than minimum of right node
    else:
        if left.state == True and right.state == True and node.value >= left.max and node.value < right.min:
            node_data = data(node, True, right.node_count + left.node_count + 1, left.min, right.max)
        else:
            node_data = data(
                    left.BSTroot if left.node_count > right.node_count else right.BSTroot,
                    False,
                    right.node_count if right.node_count > left.node_count else left.node_count,
                    None,
                    None)
    return node_data

# TEST CODE
# Shows the biggest bubble sorted subtree available in the tree
test_tree = tree(4, is_perfect = True) # a random tree with height 4. 'test_tree' currently is pointing to the root of the tree
result = BST_check(test_tree)

print(test_tree) # the main tree
print(result.node_count) # number of nodes in the bst subtree
print(result.BSTroot) # the bst subtree 


# EXTRA : Finds a tree with an arbitrary height (let's say X) in which exists a subtree with an arbitrary number of nodes (let's say N) which is bubble sorted.
X = 4
N = 7
while True:
    test_tree = tree(X) # a random tree with height 9. test_tree currently is pointing to the root of the tree
    result = BST_check(test_tree)
    if result.node_count == N: # The tree should have a bubble sorted subtree which has 6 nodes
        break

print(test_tree) # prints a graphial image of the tree
print(result.node_count)
print(result.BSTroot)
