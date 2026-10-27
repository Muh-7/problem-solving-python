#7
# Divisible sum pairs: Given an array of integers and a positive integer k,
# determine the number of pairs (i, j) where i < j and ar[i] + ar[j] is divisible by k. 
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#



# Way1
def divisibleSumPairs(n, k, ar):
    # Write your code here
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j])%k ==0:
                    num +=1
    return num


# way2 'pythonic'
def divisibleSumPairs(n, k, ar):
    return sum(
        1
        for i in range(n)
        for j in range(i + 1, n)
        if (ar[i] + ar[j]) % k == 0
    )

# test
print(divisibleSumPairs( n = 6, k = 3, ar = [1, 3, 2, 6, 1, 2]))