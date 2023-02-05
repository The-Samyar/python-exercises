# This code:
#    1) Checks if the entered number if a fibonacci number
# 
#    2) Returns all fibonacci numbers up to nth index. 
#       Indexes correspond to fibonacci numbers as follows:
#         fibonacci numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#         indexes           : 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, ...
# 
#    3)
#        i. Returns the fibonacci number at nth position.
#           Same indexing is to be used as mentioned in 2)
# 
#       ii. Returns the fibonacci number at nth position, recursively.

# 1)
def is_fibonacci(number):
    if number == 0 or number == 1:
        return True
    else:
        a, b = 0, 1
        while b <= number:
            b = b + a
            a = b - a
            if b == number:
                return True
        return False

# 2) 
def fibs_upto(index):
    fib_list = [0, 1]
    if index < 2:
        return fib_list[:index]
    else:
        for i in range(0, index-2):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# 3)
# i.
def at_index(index):
    a, b = 0, 1

    if index < 2:
        return index

    else:
        for i in range(0, index-1):
            b = b + a
            a = b - a
        return b

# ii.
def at_index_recursive(number):
    if number < 2:
        return number

    return at_index_recursive(number - 1) + at_index_recursive(number - 2)

print(is_fibonacci(5))
print(fibs_upto(10))
print(at_index(7))
print(at_index_recursive(4))