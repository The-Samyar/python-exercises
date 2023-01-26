'''
What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()

How can we make it print out what we apparently want?
'''
# What will this code print out?:
# 3
# 3
# 3


# How can we make it print out what we apparently want? :


def make_functions():
    flist = []

    def wrapper(i):
        def print_i():
            print(i)
        return print_i

    for i in [1, 2, 3]:
        flist.append(wrapper(i))

    return flist

functions = make_functions()
for f in functions:
    f()
