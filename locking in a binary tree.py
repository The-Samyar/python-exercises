        # Implement locking in a binary tree. A binary tree node can be locked
        # or unlocked only if all of its descendants or ancestors are not locked.

        # Design a binary tree node class with the following methods:

        # is_locked, which returns whether the node is locked
        # lock, which attempts to lock the node. If it cannot be locked,
        # then it should return false. Otherwise, it should lock it
        # and return true.
        # unlock, which unlocks the node. If it cannot be unlocked,
        # then it should return false. Otherwise, it should unlock
        # it and return true.
        # You may augment the node to add parent pointers or any other
        # property you would like. You may assume the class is used in
        # a single-threaded program, so there is no need for actual locks
        # or mutexes. Each method should run in O(h), where h is the height of the tree.



# I used this module so I could easily print the tree visually in the terminal. To access this feature, I inherited my node class from the module's node class.
import binarytree as bt

# All of the class methods can be remade so they work more efficient, but I tried to stick to problems goal, O(h), as much as I could.
class node(bt.Node):
    def __init__(self, val=False, parent=None, left=None, right=None, locked_descendants=0):
        self.left = None
        self.right = None
        self.parent = parent
        self.val = val
        self.locked_descendants = locked_descendants

    def is_locked(self):
        return self.val
    
    # if there are 0 locked descendants then it checks if all of its ancestors are locked too
    def is_changable(self):
        if self.locked_descendants > 0:
            return False
        else:
            parent = self.parent
            while parent:
                if parent.val == True:
                    return False
                parent = parent.parent
            return True
    
    def lock(self):
        if self.is_changable():
            self.val = True
            parent = self.parent
            while parent:
                # increments all of the nodes ancestors by one
                parent.locked_descendants += 1
                parent = parent.parent
            return True
        else:
            return False
        
    def unlock(self):
        if self.is_changable():
            self.val = False
            parent = self.parent
            while parent:
                # decrements all of the nodes ancestors by one
                parent.locked_descendants -= 1
                parent = parent.parent
            return True
        else:
            return False

# Created a tree for testing purpose
root = node()
root.right = node(parent=root)
root.left = node(parent=root)
root.left.right = node(parent=root.left)
root.left.left = node(parent=root.left)
root.left.right.right = node(parent=root.left.right)
root.left.right.left = node(parent=root.left.right)
print(root)
