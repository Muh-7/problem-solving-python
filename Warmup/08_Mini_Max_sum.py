#8
# Mini Max
# Given an array of 5 integers, calculate the min and max sums using 4 of 5 elements.

#Way1
def mini_max_sum(arr):
    total_sum = sum(arr)
    max_sum = total_sum - min(arr)
    min_sum = total_sum - max(arr)
    print(min_sum, max_sum)

#Way2
def mini_max_sum_2(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))

#Way3
def mini_max_sum_3(arr):
    sorted_arr = sorted(arr)
    print(sum(sorted_arr)-sorted_arr[-1], sum(sorted_arr)-sorted_arr[0]) 

#Way4
def mini_max_sum_4(arr):
    sums = [sum(arr[:i] + arr[i+1:]) for i in range(len(arr))]
    print(min(sums), max(sums))

#Way5
def mini_max_sum_5(arr):
    total = sum(arr)
    smallest = arr[0]
    largest = arr[0]
    
    for x in arr:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    
    print(total - largest, total - smallest)



#test
mini_max_sum([1, 2, 3, 4, 5])
mini_max_sum_2([1, 2, 3, 4, 5])