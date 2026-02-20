#5
# Breaking the records: Checking if the score is higher than the max score or lower than the min score, and counting how many times it happens.

def breakingRecords(scores):
    max_score = scores[0]
    max_count = 0
    min_score = scores[0]
    min_count = 0
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]

# Way2
def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_count = min_count = 0
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
    return [max_count, min_count]

# Way3 'pythonic'
def breakingRecords(scores):
    max_score = min_score = scores[0]
    max_count = min_count = 0
    for score in scores[1:]:
        if score > max_score:
            max_score, max_count = score, max_count + 1
        elif score < min_score:
            min_score, min_count = score, min_count + 1
    return [max_count, min_count]


#test
print(breakingRecords([10, 5, 20, 20, 45, 2, 25, 1]))

# How we can think about it:
# max_score = 10
# min_score = 10
# score = 5
# score < min_score => min_score = 5, min_count = 1 
#.