#3
# Kangaroo problem: Place of two kangaroos after n jumps.

# Way1
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'
    else:
        if (x2 - x1) % (v1 - v2) == 0:
            return 'YES'
        else:
            return 'NO'
      
# Way2  
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return 'NO'
    else:
        return 'YES' if (x2 - x1) % (v1 - v2) == 0 else 'NO'

# Way3 'pythonic'
def kangaroo(x1, v1, x2, v2):
    return 'NO' if v1 <= v2 else 'YES' if (x2 - x1) % (v1 - v2) == 0 else 'NO'        
  
# Way4 'pythonic' and concise
def kangaroo(x1, v1, x2, v2):
    return 'YES' if v1 > v2 and (x2 - x1) % (v1 - v2) == 0 else 'NO'




#test
print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))


# How we can think about it:
# print(0 + 3*1)
# print(4 + 2*1)
# print(0 + 3*2)
# print(4 + 2*2)
# print(0 + 3*3)
# print(4 + 2*3)

# x = x1 + v1
# x = x2 + v2
# x1 + v1*n = x2 + v2*n
# x1 - x2 = v2*n - v1*n
# x1 - x2 = n*(v2 - v1)
# n = (x1 - x2) / (v2 - v1)
# if n is a positive integer, then they will meet at the same location after n jumps.
# if v1 <= v2, then they will never meet, because the first kangaroo will never catch up to the second kangaroo.
# if (x2 - x1) % (v1 - v2) == 0, then n is a positive integer, and they will meet at the same location after n jumps.
# if (x2 - x1) % (v1 - v2) != 0, then n is not a positive integer, and they will never meet at the same location.
# Therefore, we can check if v1 <= v2, and if so, return 'NO'. Otherwise, we can check if (x2 - x1) % (v1 - v2) == 0, and if so, return 'YES'. Otherwise, return 'NO'.
#.