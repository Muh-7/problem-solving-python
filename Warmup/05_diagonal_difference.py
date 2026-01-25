#5
# Diagonal Difference

# Way 1
def Diagonal_Difference(arr):
    right_diag = 0
    left_diag = 0
    n = len(arr) 
    
    for i in range(n):
        right_diag += arr[i][i]
        left_diag += arr[i][n - 1 - i]
    return abs(right_diag - left_diag)

# Way 2
def Diagonal_Difference_2(arr):
    right_diag = sum(arr[i][i] for i in range(len(arr)))
    left_diag = sum(arr[i][len(arr) - 1 - i] for i in range(len(arr)))
    return abs(right_diag - left_diag)

# Way 3
def Diagonal_Difference_3(arr):
    right_diag = 0
    left_diag = 0
    
    counter = 1
    for i in range(len(arr)):
        right_diag += arr[i][i]
        left_diag += arr[i][len(arr)-counter]
        counter +=1
        
    return abs(right_diag - left_diag)



#test
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]      

result = Diagonal_Difference(arr)
print(result)
result = Diagonal_Difference_2(arr)
print(result)
result = Diagonal_Difference_3(arr)
print(result)