#08
# Migratory Birds :
# Given an array of bird sightings where every element represents a bird type id,
# determine the id of the most frequently sighted type.
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
# https://www.hackerrank.com/challenges/migratory-birds/problem

# Way1
def migratoryBirds(arr):
    # Write your code here
    bird_count = {}
    for bird in arr:
        if bird in bird_count:
            bird_count[bird] += 1
        else:
            bird_count[bird] = 1

    max_count = max(bird_count.values())
    most_frequent_birds = [bird for bird, count in bird_count.items() if count == max_count]

    return min(most_frequent_birds)



# Way2 
def migratoryBirds(arr):

    l = [0] * len(arr)
    
    for i in range(len(arr)):
        l[arr[i]] +=1
    
    return l.index(max(l))


# Way3 'pythonic'
from collections import Counter

def migratoryBirds(arr):
    counts = Counter(arr)
    return min(counts, key=lambda bird: (-counts[bird], bird))



# test
print(migratoryBirds([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])) # Output: 1



