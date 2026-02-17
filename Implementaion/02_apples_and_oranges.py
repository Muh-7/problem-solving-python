#2
# Apples and Oranges

#                             0                       10        15                           25
#    ...................-a...aaa...+a..................S.........T.....................-b...bbb...+b..................

# Way1
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount = 0
    orangesCount = 0
    
    for apple in apples:
     if apple+a >=s and apple+a <=t:
         applesCount += 1
    for orange in oranges:
        if orange+b >=s and orange+b <=t:
            orangesCount +=1
    print(applesCount)
    print(orangesCount)
    
    return applesCount, orangesCount
    
# Way2
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount = 0
    orangesCount = 0
    
    for apple in apples:
        if s <= apple + a <= t:
            applesCount += 1
            
    for orange in oranges:
        if s <= orange + b <= t:
            orangesCount += 1
    
    
    print(applesCount)
    print(orangesCount)
            
    return applesCount, orangesCount

    

# Way3 'pythonic'
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount = sum(1 for apple in apples if s <= apple + a <= t)
    orangesCount = sum(1 for orange in oranges if s <= orange + b <= t)
    
    return applesCount, orangesCount



# Way4 'Pythonic also'
def countApplesAndOranges(s, t, a, b, apples, oranges):
    return (
        sum(s <= a + d <= t for d in apples),
        sum(s <= b + d <= t for d in oranges)
    )

    
    
#test 
print(countApplesAndOranges(7,11,5,15,[2,3,4],[3,2,-2]))

# How we can think about it:
# print(5 + 2)
# print(5 + 3)
# print(5 + 4)
# print(15 + 3)
# print(15 + 2)
# print(15 + -2)    
# We can also think about it as:
# for apple in [2,3,4]:
#     print(5 + apple)
# for orange in [3,2,-2]:
#     print(15 + orange).