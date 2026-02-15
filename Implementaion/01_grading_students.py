#1
# Grading Students:

def gradingStudents(grads):
    res = []
    for grad in grads:
        if grad < 38:
            res.append( grad )
        else:
            diff = 5 - grad % 5
            if diff < 3:
                res.append(grad + diff)
            else: 
                res.append(grad)
    return res

# Way2
def gradingStudents(grads):
    res = []
    for g in grads:
        if g >= 38 and (5 - g % 5) < 3:
            g += 5 - g % 5
        res.append(g)
    return res

# Way3 'pythonic'
def gradingStudents(grads):
    return [grad + 5 - grad % 5 if grad >= 38 and (5 - grad % 5) < 3 else grad for grad in grads]




#test 
print(gradingStudents([25, 37, 38, 43, 73,81, 83]))


# How we can think about it:
# print(39%5)
# print(5- (39%5))
# x = 5 - (39%5)
# print(39 + x)