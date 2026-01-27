#9
# Birthday Cake Candles

from collections import Counter #in way4

#Way1
def birthdayCakeCandles(candles):
    highest = max(candles)
    return candles.count(highest)

#Way2
def birthdayCakeCandles_2(candles):
    highest = sorted(candles)[-1]
    return candles.count(highest)

#Way3
def birthdayCakeCandles_3(candles):
    highest = candles[0]
    counter = 0
    
    for i in candles:
        if i > highest:
            highest = i
    for i in candles:
        if i == highest:
            counter +=1
    return counter

#Way4
def birthdayCakeCandles_4(candles):
    freq = Counter(candles)
    return freq[max(freq)]

#Way5
def birthdayCakeCandles_5(candles):
    highest = candles[0]
    count = 0
    for c in candles:
        if c >= highest:
            count = count + 1 if c == highest else 1
            highest = c
    return count

#Way6 (Nice)
def birthdayCakeCandles_6(candles):
    m = max(candles)
    return sum(1 for c in candles if c == m)

#test
print(birthdayCakeCandles([1, 3, 5, 5, 5,2]))    
print(birthdayCakeCandles_2([1, 3, 5, 5, 5,2]))
print(birthdayCakeCandles_3([1, 3, 5, 5, 5,2]))
print(birthdayCakeCandles_4([1, 3, 5, 5, 5,2]))
print(birthdayCakeCandles_5([1, 3, 5, 5, 5,2]))
print(birthdayCakeCandles_6([1, 3, 5, 5, 5,2]))