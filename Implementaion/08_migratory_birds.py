#08
# Migratory Birds :
# Given an array of bird sightings where every element represents a bird type id,
# determine the id of the most frequently sighted type.
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
# https://www.hackerrank.com/challenges/migratory-birds/problem


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




s = {}
s['a'] = 1
s['b'] = 2
s['c'] = 3
for i in range(10):
    if i == 5:
        s['a'] += 1 
        
print(s.keys())