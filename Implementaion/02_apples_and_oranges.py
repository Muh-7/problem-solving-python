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

    
    
    
#test 
print(countApplesAndOranges(7,11,5,15,[2,3,4],[3,2,-2]))