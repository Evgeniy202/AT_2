def task_9(arr):
    n = len(arr)
    max_right = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(max_right, temp)
    return arr

arr1 = [17, 18, 5, 4, 6, 1]
print(task_9(arr1)) 
arr2 = [400]
print(task_9(arr2)) 
