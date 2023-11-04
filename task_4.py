def task_4(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
        else:
            i += 1

arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
task_4(arr1)
print(arr1)

arr2 = [1, 2, 3]
task_4(arr2)
print(arr2) 
