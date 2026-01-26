#7
# StairCase

def staircase(n):
    for i in range(n):
        print(' ' * (n - 1 - i) + '#' * (i + 1))


#test
staircase(4)

# Explanation:
# For each row i (0 to n-1):
# - spaces = n-1-i
# - hashes = i+1
