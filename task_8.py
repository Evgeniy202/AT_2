def task_8(arr):
    n = len(arr)
    if n < 3 or arr[0] >= arr[1]:
        return False

    increasing = True
    for i in range(1, n):
        if increasing:
            if arr[i] < arr[i - 1]:
                increasing = False
            elif arr[i] == arr[i - 1]:
                return False
        else:
            if arr[i] >= arr[i - 1]:
                return False

    return not increasing

arr1 = [2, 1]
print(task_8(arr1)) 

arr2 = [3, 5, 5]
print(task_8(arr2))

arr3 = [0, 3, 2, 1]
print(task_8(arr3)) 
