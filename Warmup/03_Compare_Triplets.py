#3
# Compare to lists everyone of each other contains 3 elements

def CompareTriplets(a,b):
    alice = 0
    bob = 0 
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return (alice, bob)

#test
a =[1,2,3]
b = [3,2,1]

result = CompareTriplets(a,b)

print(result)