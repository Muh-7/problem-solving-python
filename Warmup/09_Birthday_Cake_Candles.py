#9
# Birthday Cake Candles

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
    highest = 0
    counter = 0
    
    for i in candles:
        if i > highest:
            highest = i
    for i in candles:
        if i == highest:
            counter +=1
    return counter


#test
print(birthdayCakeCandles([1, 3, 5, 5, 5,2]))    
print(birthdayCakeCandles_2([1, 3, 5, 5, 5,2]))
print(birthdayCakeCandles_3([1, 3, 5, 5, 5,2]))