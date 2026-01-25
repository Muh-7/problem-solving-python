#6
# Plus Minus

# Way1
def plus_minus(arr):
    print('Plus Minus 1')
    pos = neg = zeros = 0
    for i in arr:
        if i > 0 :
            pos +=1
        elif i < 0 :
            neg += 1
        else :
            zeros +=1
    
    print(f'{pos/len(arr):.6f}')
    print(f'{neg/len(arr):.6f}')
    print(f'{zeros/len(arr):.6f}')
    return '1'


# Way2
def plus_minus_2(arr):
    print('Plus Minus 2')
    pos = sum(1 for i in arr if i > 0)
    neg = sum(1 for i in arr if i > 0)
    zeros = sum(1 for i in arr if i == 0)

    print(f'{pos/len(arr):.6f}\n{neg/len(arr):.6f}\n{zeros/len(arr):.6f}\n')
    return '2'



#test
plus_minus([1, 1, 0, -1, -1])
plus_minus_2([1, 1, 0, -1, -1])
