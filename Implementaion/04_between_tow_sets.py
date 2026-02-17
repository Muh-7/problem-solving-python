#4
# Between two sets: Find the number of integers that are between two sets.

# Way1
def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b)+1):
        if all(i % j == 0 for j in a) and all(j % i == 0 for j in b):
            count += 1
    return count

# Way2 
def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b)+1):
        if all(i% ai == 0 for ai in a):
            if all(bj % i == 0 for bj in b):
                count += 1
    return count

#test
print(getTotalX([2, 4], [16, 32, 96]))

# How we can think about it:
# print(max([2, 4]))
# print(min([16, 32, 96]))
# print(max([2, 4]), min([16, 32, 96]))
# for i in range(4, 17):
#     print(i)      
