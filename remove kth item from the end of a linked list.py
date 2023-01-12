'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

# Note : I created linked lists from scratch for my own understanding that how a linked list works. However, there are python packages available that have linked lists already implemente in them.

# node class represents data and a "pointer" to the next object per object
class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self, head=None):
        self.head = head
        self.last_item = head
    
    # Adds a new node to the end of the linked list
    def append(self, data):
        self.last_item.next = node(data)
        self.last_item = self.last_item.next

    # Adds a new node in the list as the k'th node of the list. Note that k can be zero as in zeroth index of the list
    def insert(self, data, k):
        pointer = self.head
        if k == 0:
            self.head = node(data, pointer)
        elif k < 0:
            print(f"k can't be negative.\nEntered value of k: {k}")

        else:
            try:
                list_length = 0
                for i in range(1, k):
                    list_length += 1
                    pointer = pointer.next
                pointer.next = node(data, pointer.next)
            except AttributeError:
                print(f"Index is larger than list's length.\nLength of linked list : {list_length - 1}\n Input index : {k}")


    # Removes kth value from the end of a list. It does so by maintaining a gap between pointer and k_item until pointer reaches the end of the list, then, k_item is the k'th value from the end of the list.
    # Note that if k is zero, it means that the last item in the list has to be removed
    
    def remove_kth_value(self, k):
        pointer = self.head
        k_item = self.head
        k_item_prev = None

        for i in range(k):
            pointer = pointer.next
        
        while pointer.next != None:
            pointer = pointer.next
            k_item_prev = k_item
            k_item = k_item.next
        
        k_item_prev.next = k_item.next
        k_item.next = None

# FOR TESTING PURPOSE

ll = linked_list(node(1))
i = 2
while i != 11:
    ll.append(i)
    i += 1

ll.remove_kth_value(3)
ll.insert(88, 2)

# Showing all the nodes in the list after altering it
pointer = ll.head
while pointer != None:
    print(pointer.data)
    pointer = pointer.next
