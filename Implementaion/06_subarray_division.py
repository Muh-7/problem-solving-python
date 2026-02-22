#6
# Subarray Division: Given a chocolate bar with integers on each square, and a day and month, count how many subarrays of length month sum to day.

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

#Way2
def birthday(s, d, m):
    count = 0
    
    # نحسب أول نافذة مرة واحدة
    window_sum = sum(s[:m])
    
    if window_sum == d:
        count += 1

    # نحرك النافذة
    for i in range(m, len(s)):
        window_sum = window_sum - s[i-m] + s[i]
        
        if window_sum == d:
            count += 1

    return count

#Way3 'pythonic'
def birthday(s, d, m):
    return sum(1 for i in range(len(s) - m + 1) if sum(s[i:i+m]) == d)


#test
print(birthday([1, 2, 1, 3, 2], 3, 2))


# How we can think about it:
# s = [1, 2, 1, 3, 2]
# d = 3
# m = 2 
# i = 0 => sum(s[0:2]) = 3 => count = 1
# i = 1 => sum(s[1:3]) = 4 => count = 1
# i = 2 => sum(s[2:4]) = 4 => count = 1
# i = 3 => sum(s[3:5]) = 5 => count = 1
# i = 4 => sum(s[4:6]) => out of range => stop