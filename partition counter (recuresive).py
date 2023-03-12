# Give n and m as inputs, count the number of ways n objects can be devided into partitions using up to 
# m objects.

# for understanding the algorithm watch https://www.youtube.com/watch?v=ngCos392W4w
# Note : In this problem, the order of partitions does not matter, just like combination versus permutation 

n = 3
m = 2

def partition_counter(n, m):
    if n == 0 :
        return 1
    elif m == 0 or n < 0:
        return 0

    return partition_counter(n, m - 1) + partition_counter(n - m, m)

print(f"{partition_counter(n, m)}")
