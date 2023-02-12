'''
Given a binary tree, return the level of the tree with minimum sum.
'''
from binarytree import tree


def minimum_sum(root):

    sums = []
    nodes = [root]

    while nodes:
        next_level_nodes = []
        total = 0
        for node in nodes:
            total += node.val
            if node.left:
                next_level_nodes.append(node.left)
            
            if node.right:
                next_level_nodes.append(node.right)

        sums.append(total)
        nodes = next_level_nodes.copy()

    smallet_sum = sums[0]

    index = 0

    for i in range(len(sums)):
        if smallet_sum > sums[i]:
            smallet_sum = sums[i]
            index = i
    
    return index

root = tree(3)

print(root)
print(f"Level {minimum_sum(root)} has the minimum sum")
