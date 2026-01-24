#4
# a very big sum in python 

def aVeryBigSum(arr):
    # C++ - long long int 
    # java - Big int
    return sum(arr)


#test
arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(arr)
print(result)